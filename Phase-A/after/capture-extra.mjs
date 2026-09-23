// Visual Phase A — supplementary captures the audit baseline could not provide.
// The baseline's leaderboard screenshots were taken against an EMPTY local list
// and an empty server fixture, so the ranked-row changes (rank-1 emphasis, the
// authored energy/cross marks) had no runtime evidence in either set. These
// frames are therefore additional evidence, NOT a matched before/after pair.
import {connect,sleep,dir} from './cdp.mjs';
const c = await connect();
await c.send('Network.enable');
await c.send('Network.setBlockedURLs',{urls:['https://*']});
await c.send('Fetch.enable',{patterns:[{urlPattern:'*/api/*'}]});
c.on('Fetch.requestPaused', async e => {
  const path = new URL(e.request.url).pathname;
  const body = path.includes('/leaderboard/') && e.request.method === 'GET'
    ? { scores: [] }
    : { error: 'Blocked by local read-only Phase-A review' };
  await c.send('Fetch.fulfillRequest',{requestId:e.requestId,responseCode:e.request.method==='GET'?200:403,
    responseHeaders:[{name:'Content-Type',value:'application/json'}],
    body:Buffer.from(JSON.stringify(body)).toString('base64')});
});
async function viewport(w,h){await c.send('Emulation.setDeviceMetricsOverride',{width:w,height:h,deviceScaleFactor:1,mobile:false});await sleep(450);}
async function ready(sel,t=10000){const end=Date.now()+t;while(Date.now()<end){if(await c.evaluate(`!!document.querySelector(${JSON.stringify(sel)})`))return;await sleep(250);}throw new Error('Timed out '+sel);}
async function all(name){for(const [w,h] of [[375,667],[414,736],[1440,900]]){await viewport(w,h);await c.shot(`${name}-${w}x${h}`);}await viewport(414,736);}

await viewport(414,736);
// Seed the LOCAL leaderboard through the product's own save shape so the rows
// render exactly as a played run would. No server, no ranked attempt, no claim.
await c.evaluate(`(()=>{
  const raw = JSON.parse(localStorage.getItem('rushpi.save') || '{}');
  const mk = (score, energies, combo, hits, daysAgo) => ({
    score, energiesCollected: energies, maxCombo: combo, obstaclesHit: hits,
    dateISO: new Date(Date.now() - daysAgo*86400000).toISOString(), mode: 'daily', rulesVersion: 3,
  });
  raw.leaderboard = [mk(2480,31,14,1,0), mk(1975,26,11,3,1), mk(1640,22,9,4,2), mk(1180,17,7,6,3), mk(883,22,8,10,4)];
  localStorage.setItem('rushpi.save', JSON.stringify(raw));
})()`);
await c.send('Page.reload'); await ready('.home'); await sleep(600);
await c.click('Leaderboard'); await ready('.leaderboard'); await sleep(400);
await c.click('Local'); await sleep(500);
await all('leaderboard-local-populated');
console.log('done');
c.close();
