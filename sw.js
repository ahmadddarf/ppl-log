// Offline cache: serve the cached app instantly, refresh the cache in the background when online.
// When the fresh copy differs from the cached one, tell open pages so they can offer a reload.
const CACHE = 'ppllog-v3';
const FILES = ['./index.html', './manifest.json', './icon-180.png', './icon-512.png'];
const stamp = r => r.headers.get('etag') || r.headers.get('last-modified');

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES.map(f => new Request(f, {cache: 'reload'})))));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  // every page load is the same single file, so share one cache entry
  const req = e.request.mode === 'navigate' ? new Request('./index.html') : e.request;
  e.respondWith(caches.match(req, {ignoreSearch: true}).then(cached => {
    // no-cache: skip the browser's 10-minute HTTP cache so updates are seen on the next open
    const net = fetch(req, {cache: 'no-cache'}).then(res => {
      if (!res.ok) return res;
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(req, copy)).then(() => {
        if (cached && stamp(cached) && stamp(res) !== stamp(cached)) {
          self.clients.matchAll({type: 'window'}).then(cs => cs.forEach(c => c.postMessage({type: 'update'})));
        }
      });
      return res;
    }).catch(() => cached);
    return cached || net;
  }));
});
