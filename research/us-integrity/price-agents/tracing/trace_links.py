#!/usr/bin/env python3
"""Finite, public HTTPS transaction-link acquisition. Retrieved content is data only."""
from __future__ import annotations
import argparse
import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import heapq
from html.parser import HTMLParser
import http.client
import ipaddress
import json
from pathlib import Path
import re
import socket
import ssl
import subprocess
import sys
import time
from urllib.parse import parse_qsl, unquote, urljoin, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser

UA = 'PipeMind-Public-Research/1.0'
KINDS = {'award', 'order', 'solicitation', 'item', 'specification', 'seller_catalog', 'company_filing', 'source_documentation'}
DEFAULTS = {'max_requests': 8, 'max_pages': 5, 'max_depth': 2, 'max_redirects': 3,
            'max_bytes_per_response': 2_000_000, 'max_total_bytes': 8_000_000,
            'timeout_seconds': 10, 'max_retries': 0, 'max_links_per_page': 200}
MAXIMA = {'max_requests': 200, 'max_pages': 100, 'max_depth': 5, 'max_redirects': 5,
          'max_bytes_per_response': 8_000_000, 'max_total_bytes': 64_000_000,
          'timeout_seconds': 30, 'max_retries': 2, 'max_links_per_page': 1000}
SENSITIVE = re.compile(r'(token|secret|password|passwd|credential|authorization|auth|session|signature|api.?key|access.?key|x.amz|x.goog)', re.I)
ACTION = re.compile(r'(^|[/_.-])(login|signin|signout|logout|oauth|authorize|account|checkout|cart|subscribe|unsubscribe|delete|remove|edit|upload|submit|payment|profile|contact|admin)([/_.-]|$)', re.I)
CONTACT = re.compile(r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b|(?:\+?\d[\d ()-]{6,}\d)')
ATTACHMENT = {'.pdf', '.txt', '.json', '.xml', '.csv'}
SUPPORTED = {'text/html', 'application/xhtml+xml', 'text/plain', 'application/pdf', 'application/json', 'application/xml', 'text/xml', 'text/csv'}

class TraceError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(b):
    return hashlib.sha256(b).hexdigest()


def safe_label(value):
    return CONTACT.sub('[contact or numeric text omitted]', ' '.join(str(value).split()))[:200]


def public_ip(value):
    try:
        ip = ipaddress.ip_address(value)
    except ValueError as exc:
        raise TraceError('invalid_resolved_address') from exc
    if not ip.is_global or ip.is_multicast or ip.is_reserved or ip.is_unspecified:
        raise TraceError('nonpublic_resolved_address')
    if ip.version == 6 and (ip.ipv4_mapped or ip.sixtofour or ip.teredo):
        raise TraceError('transition_address_not_allowed')
    return str(ip)


def valid_host(host):
    if not isinstance(host, str) or not re.fullmatch(r'(?=.{3,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z][a-z0-9-]{1,62}', host):
        raise TraceError('invalid_exact_hostname')
    if host.endswith(('.localhost', '.local', '.internal', '.test', '.invalid')):
        raise TraceError('nonpublic_hostname')
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return host
    raise TraceError('literal_ip_hosts_not_allowed')


def validate_url(url, allowed_hosts, query_keys):
    if not isinstance(url, str) or len(url) > 2048 or not url.isascii() or any(ord(x) <= 32 or ord(x) == 127 for x in url) or '\\' in url:
        raise TraceError('invalid_url_characters')
    try:
        parsed = urlsplit(url)
        port = parsed.port
    except ValueError as exc:
        raise TraceError('invalid_url') from exc
    if parsed.scheme.lower() != 'https' or parsed.username is not None or parsed.password is not None:
        raise TraceError('https_without_credentials_required')
    host = (parsed.hostname or '').lower()
    valid_host(host)
    if host not in allowed_hosts or port not in (None, 443):
        raise TraceError('host_or_port_not_approved')
    decoded = unquote(parsed.path)
    if re.search(r'%[0-9A-Fa-f]{2}', decoded) or re.search(r'%(?![0-9A-Fa-f]{2})', parsed.path):
        raise TraceError('nested_or_invalid_path_encoding')
    if '\\' in decoded or any(ord(x) < 32 or ord(x) == 127 for x in decoded) or '@' in decoded or ACTION.search(decoded):
        raise TraceError('account_action_or_unsafe_path')
    if any(segment in {'.', '..'} for segment in decoded.split('/')):
        raise TraceError('ambiguous_path')
    try:
        query = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
    except ValueError as exc:
        raise TraceError('invalid_query') from exc
    approved = query_keys.get(host, [])
    for key, value in query:
        if SENSITIVE.search(key) or key.lower() in {'key', 'code', 'sid', 'sig', 'jwt', 'action', 'cmd', 'command', 'operation', 'method'}:
            raise TraceError('credential_query_not_allowed')
        if key not in approved or '@' in unquote(value) or any(ord(x) < 32 for x in key+value):
            raise TraceError('query_not_approved')
    return urlunsplit(('https', host, parsed.path or '/', parsed.query, ''))


def validate_plan(plan):
    if not isinstance(plan, dict) or plan.get('schema_version') != '1.0' or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,99}', str(plan.get('case_id', ''))):
        raise TraceError('invalid_plan_identity')
    hosts = plan.get('allowed_hosts')
    if not isinstance(hosts, list) or not 1 <= len(hosts) <= 30 or len(hosts) != len(set(hosts)):
        raise TraceError('explicit_unique_hosts_required')
    for h in hosts:
        valid_host(h)
    query_keys = plan.get('allowed_query_keys', {})
    if not isinstance(query_keys, dict) or any(h not in hosts for h in query_keys):
        raise TraceError('invalid_query_allowlist')
    for keys in query_keys.values():
        if not isinstance(keys, list) or any(not isinstance(k, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,40}', k) for k in keys):
            raise TraceError('invalid_query_keys')
    limits = dict(DEFAULTS)
    given = plan.get('limits', {})
    if not isinstance(given, dict) or set(given)-set(DEFAULTS):
        raise TraceError('unknown_limit')
    limits.update(given)
    for key, value in limits.items():
        minimum = 0 if key in {'max_depth', 'max_redirects', 'max_retries'} else 1
        if type(value) is not int or not minimum <= value <= MAXIMA[key]:
            raise TraceError('invalid_limit_'+key)
    if limits['max_total_bytes'] < 2 or limits['max_bytes_per_response'] < 2:
        raise TraceError('byte_budget_too_small')
    seeds = plan.get('seeds')
    if not isinstance(seeds, list) or not 1 <= len(seeds) <= 50:
        raise TraceError('finite_seeds_required')
    cleaned=[]
    for seed in seeds:
        if not isinstance(seed, dict) or seed.get('kind') not in KINDS:
            raise TraceError('invalid_seed_kind')
        identifiers = seed.get('identifiers', [])
        if not isinstance(identifiers, list) or len(identifiers) > 20 or any(not isinstance(x, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{3,79}', x) for x in identifiers):
            raise TraceError('invalid_identifier')
        cleaned.append({'url': validate_url(seed.get('url'), hosts, query_keys), 'kind': seed['kind'], 'identifiers': identifiers})
    return {'schema_version':'1.0','case_id':plan['case_id'],'allowed_hosts':hosts,'allowed_query_keys':query_keys,'limits':limits,'seeds':cleaned}


def resolve_public(host, timeout):
    # A subprocess makes system DNS time-bounded, unlike getaddrinfo in a worker thread.
    script = 'import socket,json,sys; print(json.dumps(sorted({x[4][0] for x in socket.getaddrinfo(sys.argv[1],443,type=socket.SOCK_STREAM)})))'
    try:
        r = subprocess.run([sys.executable, '-I', '-c', script, host], capture_output=True, text=True, timeout=timeout, check=True)
        ips = json.loads(r.stdout)
    except (subprocess.SubprocessError, ValueError) as exc:
        raise TraceError('dns_resolution_failed_or_timed_out') from exc
    if not ips:
        raise TraceError('empty_dns_answer')
    return sorted({public_ip(ip) for ip in ips}, key=lambda x: (':' in x, x))


class PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(self, host, ip, timeout):
        context=ssl.create_default_context()
        context.set_alpn_protocols(['http/1.1'])
        super().__init__(host, port=443, timeout=timeout, context=context)
        self.pinned_ip=public_ip(ip)

    def connect(self):
        raw=socket.create_connection((self.pinned_ip,443),timeout=self.timeout)
        try:
            if public_ip(raw.getpeername()[0]) != self.pinned_ip:
                raise TraceError('connected_peer_mismatch')
            self.sock=self._context.wrap_socket(raw,server_hostname=self.host)
        except Exception:
            raw.close()
            raise


@dataclass
class Response:
    status:int
    headers:dict
    body:bytes
    complete:bool


def _fetch_direct(url, ip, timeout, byte_cap):
    parsed=urlsplit(url)
    conn=PinnedHTTPSConnection(parsed.hostname,ip,timeout)
    try:
        conn.request('GET',urlunsplit(('', '', parsed.path or '/', parsed.query, '')),
                     headers={'User-Agent':UA,'Accept':'text/html,application/pdf,application/json,text/plain;q=0.8,*/*;q=0.1','Accept-Encoding':'identity','Connection':'close'})
        response=conn.getresponse()
        headers={k.lower():v for k,v in response.getheaders() if k.lower() in {'content-type','content-length','content-encoding','location','retry-after','last-modified','etag'}}
        # At most byte_cap bytes are received. The last allowed byte is a truncation sentinel.
        body=response.read(byte_cap)
        complete=len(body)<byte_cap
        if headers.get('content-length','').isdigit():
            complete=len(body)==int(headers['content-length']) and len(body)<=byte_cap
        return Response(response.status,headers,body,complete)
    finally:
        conn.close()


def fetch(url, ip, timeout, byte_cap):
    """Absolute wall-clock bound includes TLS, headers and slow body delivery."""
    worker = ("import runpy,json,base64,sys; m=runpy.run_path(sys.argv[1]); "
              "r=m['_fetch_direct'](sys.argv[2],sys.argv[3],int(sys.argv[4]),int(sys.argv[5])); "
              "print(json.dumps({'status':r.status,'headers':r.headers,'body':base64.b64encode(r.body).decode(),'complete':r.complete}))")
    command = [sys.executable, '-I', '-c', worker, str(Path(__file__).resolve()),
               url, ip, str(timeout), str(byte_cap)]
    try:
        proc = subprocess.run(command, capture_output=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError('absolute_transport_deadline') from exc
    if proc.returncode:
        raise TraceError('transport_child_failed')
    try:
        result=json.loads(proc.stdout)
        return Response(result['status'],result['headers'],base64.b64decode(result['body'],validate=True),result['complete'])
    except (ValueError,KeyError,TypeError) as exc:
        raise TraceError('invalid_transport_child_result') from exc


class LinkParser(HTMLParser):
    def __init__(self, maximum):
        super().__init__(convert_charrefs=True)
        self.maximum=maximum;self.links=[];self.current=None;self.truncated=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a' and 'href' in attrs:
            self.finish()
            if len(self.links)>=self.maximum:
                self.truncated=True;return
            self.current=[attrs['href'],'']
        elif tag in {'object','iframe','embed'}:
            value=attrs.get('data') if tag=='object' else attrs.get('src')
            if value:
                if len(self.links)<self.maximum:self.links.append({'href':value,'anchor':tag+' attachment','element':tag})
                else:self.truncated=True
    def handle_data(self,data):
        if self.current:self.current[1]=(self.current[1]+data)[:500]
    def handle_endtag(self,tag):
        if tag=='a':self.finish()
    def finish(self):
        if self.current:
            if len(self.links)<self.maximum:self.links.append({'href':self.current[0],'anchor':safe_label(self.current[1]),'raw_anchor':self.current[1],'element':'a'})
            else:self.truncated=True
            self.current=None
    def extract(self,text):
        self.feed(text);self.finish();return self.links


def exact_identifier(text, identifiers):
    decoded=unquote(text).upper()
    return next((i for i in identifiers if re.search(r'(?<![A-Z0-9])'+re.escape(i.upper())+r'(?![A-Z0-9])',decoded)),None)


def classify_link(parent, candidate, anchor, identifiers, kind):
    parsed=urlsplit(candidate);base=urlsplit(parent)
    found=exact_identifier(candidate+' '+anchor,identifiers)
    if found:return 'follow','exact_identifier',0,found
    suffix=Path(parsed.path).suffix.lower()
    same_directory=parsed.hostname==base.hostname and parsed.path.startswith(base.path.rsplit('/',1)[0]+'/')
    if kind!='source_documentation' and suffix in ATTACHMENT and same_directory and re.search(r'\b(attachment|award|order|solicitation|specification|technical|drawing|amendment|price|schedule|filing)\b',anchor,re.I):
        return 'follow','relevant_same_directory_attachment',1,None
    return 'exclude','no_exact_transaction_or_relevant_attachment_link',9,None


def retry_date(value):
    if not value:return None
    if value.strip().isdigit():
        try:return datetime.fromtimestamp(time.time()+int(value),timezone.utc).isoformat()
        except (ValueError,OverflowError):return None
    try:return parsedate_to_datetime(value).astimezone(timezone.utc).isoformat()
    except (ValueError,TypeError,OverflowError):return None


def trace(plan, resolver=resolve_public, transport=fetch):
    plan=validate_plan(plan);limits=plan['limits'];events=[];links=[];queue=[];scheduled=set();sequence=0;total_bytes=0;pages=0;robots={};last_request={};deferred_hosts={}
    def enqueue(row,priority=0):
        nonlocal sequence
        heapq.heappush(queue,(priority,sequence,row));sequence+=1
    for seed in plan['seeds']:
        if seed['url'] not in scheduled:
            scheduled.add(seed['url']);enqueue(dict(seed,depth=0,parent_url=None,anchor=None,relationship='declared_seed',redirect_chain=[],retry=0))
        else:links.append({'parent_url':None,'target_url':seed['url'],'decision':'exclude','reason':'duplicate_seed','observed_at':now()})
    def request(url,parent,relationship):
        nonlocal total_bytes
        if len(events)>=limits['max_requests'] or total_bytes>=limits['max_total_bytes']:
            return None
        event={'attempt_id':f'TRACE-{len(events)+1:04d}','url':url,'parent_url':parent,'relationship':relationship,'started_at':now(),'method':'GET','http_status':None,'network_attempted':False,'http_request_sent':False,'body_bytes_retained':False}
        events.append(event)
        try:
            url=validate_url(url,plan['allowed_hosts'],plan['allowed_query_keys']);host=urlsplit(url).hostname
            addresses=resolver(host,limits['timeout_seconds'])
            if not addresses:raise TraceError('empty_dns_answer')
            addresses=[public_ip(ip) for ip in addresses]
            event['resolved_public_addresses']=addresses;event['pinned_address']=addresses[0]
            cap=min(limits['max_bytes_per_response'],limits['max_total_bytes']-total_bytes)
            event['network_attempted']=True;event['http_request_sent']=None;last_request[host]=time.time()
            response=transport(url,addresses[0],limits['timeout_seconds'],cap)
            if not isinstance(response,Response) or len(response.body)>cap:raise TraceError('transport_exceeded_body_cap')
            total_bytes+=len(response.body)
            event.update(http_status=response.status,http_request_sent=True,received_bytes=len(response.body),response_body_sha256=digest(response.body),hash_scope='complete_received_body' if response.complete else 'received_body_prefix',response_complete=response.complete,content_type=response.headers.get('content-type','').split(';')[0].strip().lower(),content_encoding=response.headers.get('content-encoding','identity').lower())
            event['status']='received'
            return response
        except (TraceError,OSError,http.client.HTTPException,ValueError) as exc:
            event['status']='failed';event['error']=str(exc) if isinstance(exc,TraceError) else type(exc).__name__
            return None
        finally:event['finished_at']=now()
    while queue:
        _,_,row=heapq.heappop(queue);url=row['url'];host=urlsplit(url).hostname
        if len(events)>=limits['max_requests'] or total_bytes>=limits['max_total_bytes'] or pages>=limits['max_pages']:
            enqueue(row);break
        if host in deferred_hosts:
            links.append({'parent_url':row['parent_url'],'target_url':url,'decision':'defer','reason':deferred_hosts[host],'observed_at':now()});continue
        if host not in robots:
            robot_url=f'https://{host}/robots.txt';reply=request(robot_url,None,'robots_policy')
            if reply and reply.status==200 and reply.complete and len(reply.body)<=262144 and reply.headers.get('content-encoding','identity').lower()=='identity' and reply.headers.get('content-type','').split(';')[0].lower()=='text/plain' and b'<html' not in reply.body[:512].lower():
                robot_lines=reply.body.decode('utf-8',errors='replace').splitlines()
                if any(re.match(r'\s*(allow|disallow)\s*:', line, re.I) and any(char in line.split(':',1)[1].split('#',1)[0] for char in '*$') for line in robot_lines):
                    deferred_hosts[host]='complex_robots_rules_require_review';enqueue(row);continue
                rp=RobotFileParser();rp.set_url(robot_url);rp.parse(robot_lines);robots[host]=rp
            elif reply and reply.status==404:
                robots[host]=None
            else:
                deferred_hosts[host]='robots_policy_unavailable_or_denied';enqueue(row);continue
        rp=robots[host]
        if rp and not rp.can_fetch(UA,url):
            links.append({'parent_url':row['parent_url'],'target_url':url,'decision':'exclude','reason':'robots_disallow','observed_at':now()});continue
        delay=rp.crawl_delay(UA) if rp else None
        rate=rp.request_rate(UA) if rp else None
        if rate:
            if rate.requests<=0 or rate.seconds<=0:
                deferred_hosts[host]='invalid_robots_rate_requires_review';enqueue(row);continue
            delay=max(delay or 0,rate.seconds/rate.requests)
        if delay and time.time()-last_request.get(host,0)<delay:
            deferred_hosts[host]='robots_crawl_delay_requires_later_run';enqueue(row);continue
        before=len(events);reply=request(url,row['parent_url'],row['relationship'])
        if len(events)==before:enqueue(row);break
        event=events[-1];event.update(kind=row['kind'],depth=row['depth'],anchor=row['anchor'],redirect_chain=row['redirect_chain'],retry_index=row['retry'])
        if reply is None:
            if row['retry']<limits['max_retries'] and event.get('error') in {'TimeoutError','ConnectionError','ConnectionResetError','RemoteDisconnected'}:
                enqueue({**row,'retry':row['retry']+1},3)
            continue
        if reply.status in {301,302,303,307,308}:
            target=reply.headers.get('location','')
            decision={'parent_url':url,'observed_at':now(),'relationship':'redirect','anchor':None,'decision':'exclude'}
            try:
                target=validate_url(urljoin(url,target),plan['allowed_hosts'],plan['allowed_query_keys'])
                decision['target_url']=target
                if not reply.headers.get('location'):raise TraceError('missing_redirect_location')
                if len(row['redirect_chain'])>=limits['max_redirects']:raise TraceError('redirect_limit')
                if target in scheduled:raise TraceError('duplicate_or_redirect_loop')
                scheduled.add(target);decision.update(decision='follow',reason='approved_redirect')
                enqueue({**row,'url':target,'parent_url':url,'relationship':'redirect','redirect_chain':row['redirect_chain']+[url],'retry':0})
            except TraceError as exc:decision['reason']=str(exc)
            links.append(decision);continue
        if reply.status==429 or (reply.status==503 and reply.headers.get('retry-after')):
            event['retry_not_before']=retry_date(reply.headers.get('retry-after'))
            event['retry_after_valid']=event['retry_not_before'] is not None
            deferred_hosts[host]='rate_limited_requires_later_run'
            continue
        if reply.status in {500,502,503,504} and row['retry']<limits['max_retries']:
            enqueue({**row,'retry':row['retry']+1},3);continue
        if reply.status!=200:
            event['status']='http_failure';continue
        if not reply.complete:
            event['status']='body_limit_partial_not_parsed';continue
        mime=event['content_type']
        if mime not in SUPPORTED or event['content_encoding']!='identity':
            event['status']='unsupported_content_not_parsed';continue
        pages+=1;event['status']='acquired_metadata_only';event['expected_record_identity_authenticated']=False
        if mime not in {'text/html','application/xhtml+xml'}:continue
        parser=LinkParser(limits['max_links_per_page']);found=parser.extract(reply.body.decode('utf-8',errors='replace'))
        event['link_limit_reached']=parser.truncated
        for link in found:
            decision={'parent_url':url,'observed_at':event['finished_at'],'anchor':link['anchor'],'element':link['element'],'decision':'exclude','relationship':'unclassified_link'}
            try:
                target=validate_url(urljoin(url,link['href']),plan['allowed_hosts'],plan['allowed_query_keys'])
                decision['target_url']=target
                verdict,reason,priority,identifier=classify_link(url,target,link.get('raw_anchor',link['anchor']),row['identifiers'],row['kind'])
                decision.update(decision=verdict,reason=reason,exact_identifier=identifier,relationship=reason)
                if verdict=='follow':
                    if row['depth']>=limits['max_depth']:decision.update(decision='defer',reason='depth_limit')
                    elif target in scheduled:decision.update(decision='exclude',reason='duplicate_url')
                    else:
                        scheduled.add(target);enqueue({'url':target,'kind':row['kind'],'identifiers':row['identifiers'],'depth':row['depth']+1,'parent_url':url,'anchor':link['anchor'],'relationship':reason,'redirect_chain':[],'retry':0},priority)
            except TraceError as exc:decision['reason']=str(exc)
            # Invalid targets are deliberately not retained: they may contain credentials or contacts.
            links.append(decision)
    outstanding=[{'url':row['url'],'parent_url':row['parent_url'],'kind':row['kind'],'depth':row['depth'],'reason':'run_budget_exhausted'} for _,_,row in queue]
    return {'schema_version':'1.0','adapter':'pipemind-public-transaction-tracer','case_id':plan['case_id'],'completed_at':now(),'plan':plan,'attempts':events,'link_decisions':links,'outstanding':outstanding,'coverage':{'logical_attempts':len(events),'network_attempts':sum(e['network_attempted'] for e in events),'http_requests_sent_confirmed':sum(e['http_request_sent'] is True for e in events),'acquired_documents':pages,'received_body_bytes':total_bytes,'declared_seed_count':len(plan['seeds']),'frontier_complete':not outstanding and not deferred_hosts and not any(x.get('decision')=='defer' or x.get('reason')=='robots_disallow' or (x.get('relationship')=='redirect' and x.get('decision')!='follow') for x in links) and not any(e.get('link_limit_reached') for e in events) and all((e['relationship']=='robots_policy' and e.get('http_status') in {200,404}) or e.get('status')=='acquired_metadata_only' or e.get('http_status') in {301,302,303,307,308} for e in events),'failed_or_incomplete_attempts':sum(e.get('status') in {'failed','http_failure','body_limit_partial_not_parsed','unsupported_content_not_parsed'} for e in events),'complete_procurement_universe':False},'evidence_review_required':True,'scope':'Only selected request/link metadata retained. Body digests describe received bytes, not retained full documents. No prices, people, owners, misconduct or transaction facts authenticated.','retrieved_text_handling':'Untrusted data only; no code, browser scripts, instructions, forms, cookies or account actions executed.','runtime_import':'Completed audited run may be imported honestly; this adapter does not reserve runtime attempts or claim runtime budget enforcement.'}


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('plan',type=Path);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--execute',action='store_true',help='Issue the explicitly bounded public GET requests; otherwise validate plan only');args=ap.parse_args(argv)
    if args.output.exists():raise TraceError('output_exists_no_overwrite')
    raw=args.plan.read_bytes();plan=validate_plan(json.loads(raw))
    result=trace(plan) if args.execute else {'schema_version':'1.0','case_id':plan['case_id'],'validated_plan':plan,'network_requests':0,'execution':'not_requested'}
    result['input_plan_sha256']=digest(raw);result['input_hash_scope']='Exact plan file bytes';args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'output':str(args.output),'sha256':digest(args.output.read_bytes()),'coverage':result.get('coverage'),'execution':result.get('execution','finite_run_complete')}))
    return 0

if __name__=='__main__':
    try:raise SystemExit(main())
    except (TraceError,ValueError,OSError) as exc:print('Trace failed: '+str(exc),file=sys.stderr);raise SystemExit(2)
