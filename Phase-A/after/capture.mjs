import fs from 'node:fs/promises';
import {connect,sleep,dir} from './cdp.mjs';
const c=await connect();
const records=[]; const network=[];const errors=[];
c.on('Runtime.exceptionThrown',e=>errors.push(e.exceptionDetails));
c.on('Network.requestWillBeSent',e=>network.push({url:e.request.url,method:e.request.method}));
await c.send('Network.enable');
await c.send('Network.setBlockedURLs',{urls:['https://*']});
const registry=JSON.parse(await fs.readFile('registry/tokens/v2-proposal/registry.json','utf8'));
const released=JSON.parse(await fs.readFile('public/data/token-logos/release-manifest.json','utf8'));
const chosen=[...registry.entries.filter(t=>released.entries.some(e=>e.tokenId===t.tokenId)).slice(0,10),...registry.entries.filter(t=>!released.entries.some(e=>e.tokenId===t.tokenId)).slice(0,5)];
const date=new Date().toISOString().slice(0,10);
const fixture={challengeDate:date,challengeId:'local-visual-audit-fixture',rulesVersion:3,tokenChallengeVersion:1,snapshotCreatedAt:new Date().toISOString(),providerUpdatedAt:null,status:'live',rankedEligible:true,tokens:chosen.map((t,i)=>({order:i,id:t.providerIds.coingecko,symbol:t.symbol,name:t.name,imageUrl:'https://audit.invalid/'+t.tokenId+'.png',referencePriceUsd:10+i,marketCapRank:i+1,points:100+i*10,spawnTimeMs:2500+i*3500,lane:i%3})),totalTokenPointsPossible:2550,attribution:'LOCAL AUDIT FIXTURE — no market assertions'};
await fs.writeFile(new URL('daily-fixture.json',dir),JSON.stringify(fixture,null,2));
await c.send('Fetch.enable',{patterns:[{urlPattern:'*/api/*'}]});
c.on('Fetch.requestPaused',async e=>{
 const path=new URL(e.request.url).pathname;
 const body=path==='/api/market/daily-challenge'?fixture:path.includes('/leaderboard/')&&e.request.method==='GET'?{scores:[]}:{error:'Blocked by local read-only audit'};
 await c.send('Fetch.fulfillRequest',{requestId:e.requestId,responseCode:e.request.method==='GET'?200:403,responseHeaders:[{name:'Content-Type',value:'application/json'}],body:Buffer.from(JSON.stringify(body)).toString('base64')});
});
async function viewport(w=414,h=736){await c.send('Emulation.setDeviceMetricsOverride',{width:w,height:h,deviceScaleFactor:1,mobile:false});await sleep(450);}
async function ready(sel,timeout=10000){const end=Date.now()+timeout;while(Date.now()<end){if(await c.evaluate(`!!document.querySelector(${JSON.stringify(sel)})`))return;await sleep(250);}throw new Error('Timed out '+sel);}
async function all(name){for(const [w,h] of [[375,667],[414,736],[1440,900]]){await viewport(w,h);await c.shot(`${name}-${w}x${h}`);records.push({name,width:w,height:h,timestamp:new Date().toISOString(),state:await c.evaluate(`({text:document.body.innerText,canvas:document.querySelector('canvas')?.getBoundingClientRect().toJSON(),scroll:[...document.querySelectorAll('.screen')].map(e=>({class:e.className,scrollHeight:e.scrollHeight,clientHeight:e.clientHeight})),scene:window.__rushpi?.scene?.getScene('MainScene')?.mode})`)});}await viewport();}
async function home(){if(await c.evaluate(`!!document.querySelector('.home')`))return;if(await c.evaluate(`!!document.querySelector('.result--first-run')`))await c.click('Explore');else await c.selector('.screen-back');if(await c.evaluate(`!!document.querySelector('.campaign')`))await c.selector('.screen-back');await ready('.home');}
async function runResult(timeout=100000){await ready('.result',timeout);await sleep(500);}
const task=process.argv[2]||'guided';
try{
 await viewport();
 if(task==='guided'){
   await c.evaluate('localStorage.clear()');await c.send('Page.reload');await ready('canvas');await sleep(2300);await all('guided-gameplay');
   await runResult();await all('first-result');
   await c.click('Explore');await all('home');
 }else if(task==='navigation'){
   await home();await all('home');await c.click('Leaderboard');await ready('.leaderboard');await all('leaderboard-daily-empty');await c.click('Local');await all('leaderboard-local');await home();
   await c.click('Profile');await all('profile');await c.evaluate(`document.querySelector('.profile').scrollTop=500`);await all('profile-lower');await home();
   await c.selector('[aria-label="How to play Daily Run"]');await all('daily-intro-modal');await c.selector('.intro-modal .btn--primary');await ready('.daily-prep');await sleep(1500);await all('daily-preparation');
 }else if(task==='daily'){
   if(!await c.evaluate(`!!document.querySelector('.daily-prep')`)){await home();await c.selector('.mode-card--primary');await ready('.daily-prep');await sleep(1500);}
   await all('daily-preparation');await c.click('Play locally');await ready('canvas');await sleep(4000);await all('daily-gameplay');
   await sleep(8000);await all('daily-midrun');
   await runResult();await all('daily-result');
   await c.selector('.result__details summary');await c.evaluate(`document.querySelector('.result').scrollTop=1000`);await all('token-detail');
 }else if(task==='survey'){
   await home();await c.selector('.mode-card--primary');await ready('.daily-prep');await sleep(1500);await c.click('Play locally');await ready('canvas');
   const milestones=[1000,21000,28000,39000,44000,51000,60000];let next=0;
   const until=Date.now()+120000;
   while(Date.now()<until){
     const state=await c.evaluate(`(()=>{const g=window.__rushpi,s=g?.scene?.getScene('MainScene');return {elapsed:s?.elapsedMs,runState:s?.runState,mode:s?.mode,playerX:s?.player?.x,lane:s?.currentLane,objects:s?.objects?.filter(o=>o.alive).map(o=>({type:o.type,token:o.tokenSpec?.id,x:o.container.x,y:o.container.y})),textures:g?.textures?.getTextureKeys(),hud:s?.lastHud,result:!!document.querySelector('.result')}})()`);
     records.push({sample:true,...state});
     if(state.result)break;
     if(next<milestones.length&&state.elapsed>=milestones[next]){await c.shot(`daily-survey-${milestones[next]}ms-414x736`);next++;}
     if(state.elapsed>5000&&state.elapsed<5500){await c.send('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});await c.send('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});}
     await sleep(250);
   }
   await all('daily-repeat-result');
 }else if(task==='training'){
   await home();await c.click('Training');await ready('canvas');await sleep(3000);await all('training-gameplay');
   await c.selector('.screen-back');await all('quit-modal');
   console.log('QUIT BUTTONS',await c.evaluate(`[...document.querySelectorAll('button')].map(b=>b.innerText)`));
 }else if(task==='survival'||task==='campaign'){
   await c.evaluate(`localStorage.setItem('rushpi:onboarding:${task}:v1','1')`);
   await home();await c.selector(task==='survival'?'.home__modes-row .mode-wrap:first-child .mode-card':'.home__modes-row .mode-wrap:last-child .mode-card');
   if(task==='campaign'){await ready('.campaign');await all('campaign');await c.selector('.level-card.is-unlocked');}
   await ready('canvas');await sleep(3500);await all(task+'-gameplay');await runResult(180000);await all(task+'-result');
 }else if(task==='training-result'){
   if(await c.evaluate(`document.body.innerText.includes('Keep playing')`))await c.click('Keep playing');
   await runResult();await all('training-result');
 }
}finally{
 await fs.writeFile(new URL(`capture-log-${task}.json`,dir),JSON.stringify({task,records,errors,network},null,2));
 c.close();
}
