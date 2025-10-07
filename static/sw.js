// Service Worker for REMC PWA - Native App Experience
const CACHE_NAME = 'remc-pwa-v2';
const STATIC_CACHE = 'remc-static-v2';
const DYNAMIC_CACHE = 'remc-dynamic-v2';

const urlsToCache = [
  '/',
  '/projects',
  '/emails',
  '/help',
  '/settings',
  '/install',
  '/static/manifest.json',
  '/static/icon-192.svg',
  '/static/sw.js',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'
];

// Install event - cache critical resources
self.addEventListener('install', function(event) {
  console.log('REMC Service Worker: Installing...');
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(function(cache) {
        console.log('REMC Service Worker: Caching app shell');
        return cache.addAll(urlsToCache);
      })
      .then(() => {
        console.log('REMC Service Worker: Installed successfully');
        return self.skipWaiting(); // Activate immediately
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', function(event) {
  console.log('REMC Service Worker: Activating...');
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
            console.log('REMC Service Worker: Deleting old cache', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      console.log('REMC Service Worker: Activated successfully');
      return self.clients.claim(); // Take control immediately
    })
  );
});

// Fetch event - serve from cache with network fallback
self.addEventListener('fetch', function(event) {
  const requestUrl = new URL(event.request.url);
  
  // Handle API requests with network-first strategy
  if (requestUrl.pathname.startsWith('/api/')) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          // Clone response for cache
          const responseClone = response.clone();
          caches.open(DYNAMIC_CACHE).then(cache => {
            cache.put(event.request, responseClone);
          });
          return response;
        })
        .catch(() => {
          // Fallback to cache if network fails
          return caches.match(event.request);
        })
    );
    return;
  }
  
  // Handle all other requests with cache-first strategy
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        if (response) {
          console.log('REMC Service Worker: Serving from cache', event.request.url);
          return response;
        }
        
        console.log('REMC Service Worker: Fetching from network', event.request.url);
        return fetch(event.request).then(response => {
          // Don't cache non-successful responses
          if (!response || response.status !== 200 || response.type !== 'basic') {
            return response;
          }
          
          // Clone the response for caching
          const responseToCache = response.clone();
          caches.open(DYNAMIC_CACHE).then(cache => {
            cache.put(event.request, responseToCache);
          });
          
          return response;
        });
      })
      .catch(error => {
        console.log('REMC Service Worker: Fetch failed', error);
        // Return offline page for navigation requests
        if (event.request.destination === 'document') {
          return caches.match('/');
        }
      })
  );
});

// Background sync for when app comes back online
self.addEventListener('sync', function(event) {
  console.log('REMC Service Worker: Background sync triggered');
  if (event.tag === 'remc-sync') {
    event.waitUntil(
      // Sync any pending data when back online
      syncPendingData()
    );
  }
});

// Push notifications support
self.addEventListener('push', function(event) {
  console.log('REMC Service Worker: Push notification received');
  const options = {
    body: event.data ? event.data.text() : 'New REMC notification',
    icon: '/static/icon-192.svg',
    badge: '/static/icon-192.svg',
    vibrate: [200, 100, 200],
    data: {
      dateOfArrival: Date.now(),
      primaryKey: 1
    },
    actions: [
      {
        action: 'explore',
        title: 'Open REMC',
        icon: '/static/icon-192.svg'
      },
      {
        action: 'close',
        title: 'Close',
        icon: '/static/icon-192.svg'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('REMC', options)
  );
});

// Handle notification clicks
self.addEventListener('notificationclick', function(event) {
  console.log('REMC Service Worker: Notification clicked');
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow('/')
    );
  }
});

function syncPendingData() {
  // Placeholder for syncing offline data
  return Promise.resolve();
}