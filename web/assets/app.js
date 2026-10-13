/* PipeMind AI research workbench. No token persisted, no direct OT actions. */
(function () {
  'use strict';
  let token = '';
  let lastTank = null;
  let lastCable = null;
  let toastTimer = null;
  const $ = (s) => document.querySelector(s);
  const $$ = (s) => Array.from(document.querySelectorAll(s));
  const views = {
    overview: 'Command centre', tank: 'LH₂ tank twin', cable: 'Hybrid cable',
    economics: 'Economics', research: 'Research brain', agents: 'AI specialists',
    security: 'Security & APEX'
  };
  const fmt = (value, dp=1) => typeof value === 'number' && Number.isFinite(value)
    ? value.toLocaleString('en-GB', {maximumFractionDigits:dp, minimumFractionDigits:dp}) : '—';
  const say = (selector, text) => { const node = $(selector); if (node) node.textContent = String(text); };
  const toast = (message) => {
    const node = $('#toast');
    node.textContent = String(message);
    node.classList.add('visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => node.classList.remove('visible'), 5500);
  };
  async function api(path, method, body) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 30000);
    try {
      const res = await fetch('/api/v1' + path, {
        method: method || 'GET',
        headers: {'Authorization': 'Bearer ' + token, ...(body ? {'Content-Type': 'application/json'} : {})},
        body: body ? JSON.stringify(body) : undefined,
        signal: controller.signal,
        credentials: 'omit'
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || data.error || 'Request rejected');
      return data;
    } finally { clearTimeout(timeout); }
  }
  const serializeForm = (form) => {
    const obj = {};
    new FormData(form).forEach((value, key) => {
      obj[key] = key === 'spin' ? value : Number(value);
    });
    return obj;
  };
  function view(page) {
    if (!views[page]) return;
    $$('.page').forEach(el => el.classList.toggle('active', el.id === 'view-' + page));
    $$('.nav-link').forEach(el => el.classList.toggle('active', el.dataset.view === page));
    say('#page-name', views[page]);
    window.scrollTo({top:0,behavior:'smooth'});
  }
  function drawPlot(canvas, datasets, xkey, ykeys, units) {
    if (!canvas || !datasets.length) return;
    const w = Math.max(320, Math.round(canvas.clientWidth || 500));
    const h = Number(canvas.getAttribute('height')) || 260;
    const dpr = Math.min(window.devicePixelRatio || 1,2);
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    const c = canvas.getContext('2d');
    c.scale(dpr, dpr);
    c.clearRect(0,0,w,h);
    const pad = {l:52,r:15,t:23,b:37};
    const cw=w-pad.l-pad.r,ch=h-pad.t-pad.b;
    const xs=datasets.map(x => Number(x[xkey]));
    const xmin=Math.min(...xs),xmax=Math.max(...xs);
    if (!Number.isFinite(xmin) || xmax===xmin) return;
    c.font='11px system-ui';
    c.textAlign='right';
    c.strokeStyle='#eaf0f7';
    c.fillStyle='#94a2b6';
    for(let j=0;j<=4;j++){
      const y=pad.t+ch*j/4;
      c.beginPath();c.moveTo(pad.l,y);c.lineTo(w-pad.r,y);c.stroke();
    }
    const colors=['#5174eb','#8d73da'];
    ykeys.forEach((key, k) => {
      const raw=datasets.map(d=>Number(d[key]));
      if (raw.some(y=>!Number.isFinite(y))) return;
      const ylo=Math.min(...raw),yhi=Math.max(...raw),ymargin=Math.max(1e-8,Math.abs(yhi-ylo)*.12);
      const low=ylo-ymargin,high=yhi+ymargin;
      const xscale=x=>pad.l+cw*(x-xmin)/(xmax-xmin);
      const yscale=y=>pad.t+ch-(y-low)/(high-low)*ch;
      c.lineWidth=2.5;c.strokeStyle=colors[k%colors.length];c.beginPath();
      raw.forEach((value,i)=>{if(i===0)c.moveTo(xscale(xs[i]),yscale(value));else c.lineTo(xscale(xs[i]),yscale(value));});
      c.stroke();
      if(k===0) {
        c.fillStyle='#889bb1';
        for(let j=0;j<=4;j++){
          const v=high-(high-low)*j/4;
          c.fillText(fmt(v,Math.abs(high-low)>100?0:2),pad.l-9,pad.t+ch*j/4+4);
        }
      }
    });
    c.textAlign='center';c.fillStyle='#96a5b8';
    for(let j=0;j<=4;j++){const value=xmin+(xmax-xmin)*j/4;c.fillText(fmt(value,1),pad.l+cw*j/4,h-13);}
    c.fillStyle='#526380';c.textAlign='left';c.fillText(units||'',pad.l,pad.t-9);
  }
  function tankPlot() {
    if (!lastTank) return;
    const points=lastTank.points.map(p=>({...p,pressure_kpa:p.pressure_pa/1000}));
    drawPlot($('#tank-chart'),points,'hour',['pressure_kpa'],'Pressure · kPa');
    drawPlot($('#overview-chart'),points,'hour',['pressure_kpa','temperature_k'],'Pressure kPa / Temperature K');
  }
  function cablePlot() {
    if (!lastCable) return;
    drawPlot($('#cable-chart'),lastCable.points,'metres',['temperature_k'],'Temperature · K');
  }
  function handleTank(run){
    lastTank=run;
    const points=run.points;
    const final=points[points.length-1];
    say('#metric-pressure',fmt(final.pressure_pa/1000,1));
    say('#metric-inventory',fmt(run.initial_mass_kg,0));
    say('#metric-heat',fmt(run.input.heat_ingress_w,0));
    say('#metric-pressure-note','Simulated endpoint · '+fmt(final.hour,1)+' h');
    say('#tank-end-pressure',fmt(final.pressure_pa/1000,1)+' kPa');
    say('#tank-cooling',fmt(run.refrigeration_electricity_kwh,2)+' kWh');
    say('#tank-eos',run.eos_version);
    say('#tank-result-id','Run '+String(run.run_id||'').slice(0,8));
    say('#chart-explainer','Well-mixed two-phase equilibrium · '+run.input.spin+
      ' hydrogen · not a certified tank pressure forecast');
    const liquidHeight=140*run.input.fill_liquid_volume_fraction;
    const top=218-liquidHeight;
    $('#tank-liquid').setAttribute('y',String(top));
    $('#tank-liquid').setAttribute('height',String(liquidHeight+5));
    $('#tank-surface').setAttribute('cy',String(top));
    tankPlot();
  }
  function handleCable(run){
    lastCable=run;
    say('#metric-margin',fmt(run.minimum_saturation_margin_k,2));
    say('#cable-end-temp',fmt(run.outlet_temperature_k,2)+' K');
    say('#cable-drop',fmt((run.input.inlet_pressure_pa-run.outlet_pressure_pa)/1000,2)+' kPa');
    say('#cable-margin',fmt(run.minimum_saturation_margin_k,2)+' K');
    cablePlot();
  }
  function withSubmit(selector,path,handler) {
    $(selector).addEventListener('submit',async e=>{
      e.preventDefault();
      const form=e.currentTarget, button=form.querySelector('button[type=submit]');
      button.disabled=true;
      try{const result=await api(path,'POST',serializeForm(form));handler(result);toast('Scenario complete. Result recorded in the audit trail.');}
      catch(err){toast('Model rejected: '+err.message);}
      finally{button.disabled=false;}
    });
  }
  async function doResearch(event) {
    event.preventDefault();
    const question=new FormData(event.currentTarget).get('question');
    const out=$('#research-results');
    out.textContent='Searching reviewed and unreviewed notes…';
    try{
      const data=await api('/research/search','POST',{question:String(question),limit:12});
      out.textContent='';
      if(!data.results.length){out.textContent='No matching passages found.';return;}
      data.results.forEach(hit=>{
        const article=document.createElement('article');article.className='research-hit';
        const h=document.createElement('h3');h.textContent=hit.heading;
        const p=document.createElement('p');p.textContent=hit.snippet;
        const sm=document.createElement('small');sm.textContent=hit.path+' · lines '+hit.start_line+'–'+hit.end_line;
        const a=document.createElement('a');a.textContent='View source in GitHub →';
        a.href='https://github.com/charlie1906clark-del/pipemind-ai/blob/main/'+hit.path.split('/').map(encodeURIComponent).join('/')+'#L'+hit.start_line;
        a.target='_blank';a.rel='noopener noreferrer';
        article.append(h,sm,p,a);out.append(article);
      });
    }catch(err){out.textContent=err.message;}
  }
  $('#nav').addEventListener('click',event=>{const target=event.target.closest('[data-view]');if(target)view(target.dataset.view);});
  $$('.sidebar [data-view]').forEach(button=>button.addEventListener('click',()=>view(button.dataset.view)));
  $('#login-form').addEventListener('submit',async e=>{
    e.preventDefault();const value=$('#token-field').value.trim();token=value;
    try{
      const status=await api('/status','GET');
      say('#tenant-label',status.tenant);
      say('#platform-mode','Connected · '+status.tenant);
      $('#login-overlay').classList.add('hidden');$('#token-field').value='';
      toast('Authenticated research environment · no equipment control');
    }catch(err){token='';say('#login-error',err.message);}
  });
  $('#change-token').addEventListener('click',()=>{$('#login-overlay').classList.remove('hidden');token='';say('#tenant-label','Not signed in');});
  withSubmit('#tank-form','/simulations/tank',handleTank);
  withSubmit('#cable-form','/simulations/cable',handleCable);
  withSubmit('#cost-form','/cost/evaluate',(r)=>{
    say('#cost-total','£'+fmt(r.total_modelled_cost_gbp,2));
    say('#cost-gross',fmt(r.gross_vapour_equivalent_kg,1)+' kg');
    say('#cost-lost',fmt(r.unrecovered_equivalent_kg,1)+' kg');
    say('#cost-electric',fmt(r.cooling_electricity_kwh,1)+' kWh');
  });
  $('#research-form').addEventListener('submit',doResearch);
  $('#verify-audit').addEventListener('click',async()=>{
    try{const result=await api('/audit/verify','GET');say('#audit-response',result.verified?
      'Chain verified · '+result.event_count+' events · head '+result.chain_head.slice(0,12):
      'Verification failed at event '+result.failed_sequence);}
    catch(err){say('#audit-response',err.message);}
  });
  function plotBlank(){
    [$('#overview-chart'),$('#tank-chart'),$('#cable-chart')].forEach(canvas=>{
      const w=Math.max(320,canvas.clientWidth||500),h=Number(canvas.getAttribute('height'))||245,dpr=window.devicePixelRatio||1;
      canvas.width=w*dpr;canvas.height=h*dpr;const c=canvas.getContext('2d');c.scale(dpr,dpr);
      c.clearRect(0,0,w,h);c.strokeStyle='#edf1f6';
      for(let i=0;i<5;i++){c.beginPath();c.moveTo(50,23+i*(h-60)/4);c.lineTo(w-20,23+i*(h-60)/4);c.stroke();}
      c.fillStyle='#b0bccd';c.font='12px system-ui';c.textAlign='center';c.fillText('Run a simulation to populate this chart',w/2,h/2);
    });
  }
  window.addEventListener('resize',()=>{
    if(lastTank) tankPlot();
    if(lastCable) cablePlot();
    if(!lastTank&&!lastCable)plotBlank();
  });
  plotBlank();
})();
