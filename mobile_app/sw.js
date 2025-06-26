const CACHE_NAME = 'obra-cache-v1';
const FILES = [
    '/',
    '/index.html',
    '/style.css',
    '/app.js',
    '/config.js'
];
self.addEventListener('install', evt => {
    evt.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(FILES))
    );
});
self.addEventListener('fetch', evt => {
    evt.respondWith(
        caches.match(evt.request).then(response => response || fetch(evt.request))
    );
});
