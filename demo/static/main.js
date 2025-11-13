
async function callNowcast() {
  const d = document.getElementById('district').value;
  const r = await fetch(`/api/nowcast?district=${encodeURIComponent(d)}`);
  document.getElementById('nowcastOut').textContent = JSON.stringify(await r.json(), null, 2);
}
async function callFlood() {
  const p = document.getElementById('poly').value;
  const r = await fetch(`/api/flood_risk?polyline_id=${encodeURIComponent(p)}`);
  document.getElementById('floodOut').textContent = JSON.stringify(await r.json(), null, 2);
}
async function callGeo() {
  const q = document.getElementById('addr').value;
  const r = await fetch(`/api/geocode?q=${encodeURIComponent(q)}`);
  document.getElementById('geoOut').textContent = JSON.stringify(await r.json(), null, 2);
}
async function callWater() {
  const m = document.getElementById('meter').value;
  const r = await fetch(`/api/water/anomaly?meter_id=${encodeURIComponent(m)}`);
  document.getElementById('waterOut').textContent = JSON.stringify(await r.json(), null, 2);
}
async function callSchool() {
  const f = document.getElementById('file').files[0];
  if (!f) { alert('Pick an image'); return; }
  const form = new FormData();
  form.append('file', f);
  const r = await fetch(`/api/school/risk`, { method: 'POST', body: form });
  document.getElementById('schoolOut').textContent = JSON.stringify(await r.json(), null, 2);
}
