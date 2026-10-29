#!/usr/bin/env python3
"""Repeat the public identifier checks; save only the explicitly allowed fields.
Usage: python acquire_identity.py /path/to/new-snapshot-directory
Never writes full NPPES/LEIE responses, streets, postcodes, phone, DOB or individual LEIE rows.
"""
import argparse, csv, hashlib, io, json, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

NPIS = ('1790533503', '1609626167')
HOSTS = {'npiregistry.cms.hhs.gov', 'data.colorado.gov', 'oig.hhs.gov'}

def fetch(url):
    if urllib.parse.urlparse(url).hostname not in HOSTS:
        raise ValueError('Source host is outside this bounded audit')
    with urllib.request.urlopen(url, timeout=45) as response:
        if urllib.parse.urlparse(response.url).hostname not in HOSTS:
            raise ValueError('Unexpected redirect host')
        payload = response.read(25_000_001)
    if len(payload) > 25_000_000:
        raise ValueError('Response exceeds audit byte limit')
    return payload, {
        'source_url': url,
        'retrieved_at': datetime.now(timezone.utc).isoformat(),
        'sha256_original_response': hashlib.sha256(payload).hexdigest(),
        'raw_response_archived': False,
        'original_byte_length': len(payload),
    }

def save(directory, name, record):
    (directory / name).write_text(json.dumps(record, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_directory', type=Path)
    directory = parser.parse_args().output_directory
    directory.mkdir(parents=True, exist_ok=False)
    for npi in NPIS:
        raw, manifest = fetch('https://npiregistry.cms.hhs.gov/api/?version=2.1&number=' + npi)
        data = json.loads(raw)
        records = []
        basic_fields = {'organization_name', 'organizational_subpart', 'enumeration_date',
                        'last_updated', 'certification_date', 'status', 'authorized_official_first_name',
                        'authorized_official_middle_name', 'authorized_official_last_name',
                        'authorized_official_title_or_position'}
        for item in data.get('results', []):
            if str(item.get('number')) != npi or item.get('enumeration_type') != 'NPI-2':
                raise ValueError('Unexpected identifier or person record')
            records.append({'number': npi, 'enumeration_type': item['enumeration_type'],
                            'basic': {k:v for k,v in item.get('basic', {}).items() if k in basic_fields},
                            'locations': [{k:v for k,v in a.items() if k in {'address_purpose','city','state','country_code'}} for a in item.get('addresses', [])],
                            'taxonomy_codes': [a['code'] for a in item.get('taxonomies', [])],
                            'other_names': item.get('other_names', [])})
        manifest.update(result_count=data.get('result_count'), results=records)
        save(directory, 'nppes_' + npi + '.json', manifest)
    query = urllib.parse.urlencode({'$where': "entityid='20241008944'", '$select':
        'entityid,entityname,entitystatus,jurisdictonofformation,entitytype,entityformdate,principalcity,principalstate,agentfirstname,agentlastname'})
    raw, manifest = fetch('https://data.colorado.gov/resource/4ykn-tg5h.json?' + query)
    manifest['data'] = json.loads(raw)
    save(directory, 'colorado_snapshot.json', manifest)
    raw, manifest = fetch('https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv')
    matched = []; count = 0
    fields = {'BUSNAME','GENERAL','SPECIALTY','NPI','STATE','EXCLTYPE','EXCLDATE','REINDATE','WAIVERDATE','WVRSTATE'}
    for row in csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))):
        count += 1
        if row.get('NPI') in NPIS and row.get('BUSNAME'):
            matched.append({k:v for k,v in row.items() if k in fields})
    manifest.update(rows_scanned=count, searched_npis=list(NPIS), matches=matched,
                    scope='Active-exclusion snapshot. Missing exact-NPI match is not clearance; consult source coverage date.')
    save(directory, 'leie_snapshot.json', manifest)
    print(json.dumps({'status':'complete', 'output_directory':str(directory), 'npi_checks':len(NPIS), 'leie_matches':len(matched)}))

if __name__ == '__main__':
    main()
