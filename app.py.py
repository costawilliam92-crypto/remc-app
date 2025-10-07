"""
REMC Web App - Simplified Railway Deployment Version
Single file with everything embedded for guaranteed deployment
"""

from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Sample data embedded in the app
SAMPLE_PROJECTS = [
    {
        "id": "proj_001",
        "project_name": "Highway Construction Phase 1",
        "client_name": "City Council",
        "status": "In Progress",
        "quote_value": 450000.00,
        "start_date": "2024-01-15",
        "completion_date": "2024-08-30"
    },
    {
        "id": "proj_002", 
        "project_name": "Shopping Center Development",
        "client_name": "Retail Group Ltd",
        "status": "Quoted",
        "quote_value": 280000.00,
        "start_date": "2024-03-01",
        "completion_date": "2024-10-15"
    },
    {
        "id": "proj_003",
        "project_name": "Residential Subdivision",
        "client_name": "Housing Corp",
        "status": "Completed",
        "quote_value": 650000.00,
        "start_date": "2023-08-01",
        "completion_date": "2024-02-28"
    }
]

@app.route('/')
def index():
    """Main page with deployment success and install links"""
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>REMC - Deployed Successfully!</title>
        <meta name="theme-color" content="#1a472a">
        <link rel="manifest" href="/manifest.json">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #1a472a, #2d5a3d);
                color: white;
                margin: 0;
                padding: 20px;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .container {{
                text-align: center;
                max-width: 500px;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            }}
            h1 {{ color: #ffd700; margin-bottom: 20px; font-size: 2.5em; }}
            .success {{ color: #28a745; font-size: 1.3em; margin: 20px 0; }}
            .btn {{
                background: #ffd700;
                color: #1a472a;
                padding: 18px 35px;
                border: none;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                font-size: 1.2em;
                display: inline-block;
                margin: 15px 10px;
                cursor: pointer;
                transition: all 0.3s ease;
                min-width: 200px;
            }}
            .btn:hover {{ background: #ffed4e; transform: translateY(-2px); }}
            .btn.secondary {{ background: #28a745; color: white; }}
            .url-info {{
                margin-top: 30px;
                font-size: 0.9em;
                opacity: 0.8;
                background: rgba(0,0,0,0.2);
                padding: 20px;
                border-radius: 10px;
            }}
            .emoji {{ font-size: 3em; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🏗️</div>
            <h1>REMC Deployed!</h1>
            <div class="success">✅ Railway Deployment Successful!</div>
            <p>REMC Project Management is now globally accessible</p>
            
            <a href="/install" class="btn">📱 Install as App</a>
            <a href="/projects" class="btn secondary">📋 View Projects</a>
            
            <div class="url-info">
                <p><strong>🌍 Global URL:</strong><br>{request.url_root}</p>
                <p><strong>📲 Install URL:</strong><br>{request.url_root}install</p>
                <p><strong>📋 Projects URL:</strong><br>{request.url_root}projects</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/install')
def install_page():
    """PWA Installation page optimized for mobile"""
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Install REMC App</title>
        <link rel="manifest" href="/manifest.json">
        <meta name="theme-color" content="#1a472a">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="default">
        <meta name="apple-mobile-web-app-title" content="REMC">
        <link rel="apple-touch-icon" href="/icon-192x192.png">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #1a472a, #2d5a3d);
                color: white;
                margin: 0;
                padding: 20px;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .container {{
                text-align: center;
                max-width: 450px;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 25px 50px rgba(0,0,0,0.3);
            }}
            h1 {{ color: #ffd700; margin-bottom: 30px; font-size: 2.2em; }}
            .app-icon {{
                width: 120px;
                height: 120px;
                margin: 0 auto 30px;
                background: #ffd700;
                border-radius: 25px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 4em;
                animation: bounce 2s infinite;
            }}
            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                40% {{ transform: translateY(-10px); }}
                60% {{ transform: translateY(-5px); }}
            }}
            .install-btn {{
                background: #ffd700;
                color: #1a472a;
                padding: 18px 30px;
                border: none;
                border-radius: 12px;
                font-weight: bold;
                font-size: 1.3em;
                cursor: pointer;
                width: 100%;
                margin-bottom: 15px;
                text-decoration: none;
                display: inline-block;
                transition: all 0.3s ease;
            }}
            .install-btn:hover {{ background: #ffed4e; transform: translateY(-2px); }}
            .install-btn:disabled {{ 
                background: #ccc; 
                color: #666; 
                cursor: not-allowed; 
                transform: none;
            }}
            .web-btn {{
                background: #28a745;
                color: white;
                padding: 15px 30px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                font-size: 1.1em;
                cursor: pointer;
                width: 100%;
                margin-bottom: 15px;
                text-decoration: none;
                display: inline-block;
            }}
            .manual-steps {{
                margin-top: 30px;
                text-align: left;
                background: rgba(0,0,0,0.2);
                padding: 25px;
                border-radius: 12px;
                font-size: 0.95em;
            }}
            .platform {{ 
                margin-bottom: 20px; 
                padding: 15px;
                background: rgba(255,255,255,0.05);
                border-radius: 8px;
            }}
            .platform strong {{ color: #ffd700; font-size: 1.1em; }}
            .status {{
                margin: 15px 0;
                padding: 12px;
                border-radius: 8px;
                font-weight: bold;
                text-align: center;
            }}
            .success {{ background: rgba(40, 167, 69, 0.3); color: #28a745; }}
            .error {{ background: rgba(220, 53, 69, 0.3); color: #dc3545; }}
            .warning {{ background: rgba(255, 193, 7, 0.3); color: #ffc107; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="app-icon">🏗️</div>
            <h1>Install REMC App</h1>
            <p>Get the full native app experience on your device!</p>
            
            <div id="status"></div>
            
            <button id="installBtn" class="install-btn" onclick="installApp()">
                📱 Install Native App
            </button>
            
            <a href="/projects" class="web-btn">
                🌐 Use Web Version
            </a>
            
            <div class="manual-steps">
                <h3 style="color: #ffd700; margin-top: 0;">📋 Manual Installation Steps:</h3>
                
                <div class="platform">
                    <strong>📱 iPhone/iPad (Safari):</strong><br>
                    1. Tap the Share button (□↗) at the bottom<br>
                    2. Scroll down and tap "Add to Home Screen"<br>
                    3. Tap "Add" to confirm<br>
                    4. App will appear on your home screen!
                </div>
                
                <div class="platform">
                    <strong>🤖 Android (Chrome):</strong><br>
                    1. Tap the menu button (⋮) in the top right<br>
                    2. Tap "Add to Home Screen"<br>
                    3. Tap "Add" to confirm<br>
                    4. App will install like a regular app!
                </div>
                
                <div class="platform">
                    <strong>💻 Desktop (Chrome/Edge):</strong><br>
                    1. Look for the install icon in the address bar<br>
                    2. Or use menu → "Install REMC App"<br>
                    3. Click "Install" to add to your desktop
                </div>
            </div>
        </div>

        <script>
            let deferredPrompt;
            const installBtn = document.getElementById('installBtn');
            const status = document.getElementById('status');

            // Check if app is already installed
            window.addEventListener('appinstalled', () => {{
                showStatus('🎉 App installed successfully! Check your home screen!', 'success');
                installBtn.style.display = 'none';
            }});

            // Capture the install prompt
            window.addEventListener('beforeinstallprompt', (e) => {{
                e.preventDefault();
                deferredPrompt = e;
                installBtn.style.display = 'block';
                showStatus('✅ App is ready for installation!', 'success');
            }});

            function installApp() {{
                if (deferredPrompt) {{
                    deferredPrompt.prompt();
                    deferredPrompt.userChoice.then((choiceResult) => {{
                        if (choiceResult.outcome === 'accepted') {{
                            showStatus('📥 Installing app...', 'warning');
                        }} else {{
                            showStatus('❌ Installation cancelled', 'error');
                        }}
                        deferredPrompt = null;
                    }});
                }} else {{
                    showStatus('📋 Please use the manual installation steps below', 'warning');
                }}
            }}

            function showStatus(message, type) {{
                status.innerHTML = `<div class="status ${{type}}">${{message}}</div>`;
            }}

            // Check if running in standalone mode (already installed)
            if (window.navigator.standalone || window.matchMedia('(display-mode: standalone)').matches) {{
                showStatus('🏠 App is running in native mode!', 'success');
                installBtn.innerHTML = '✅ Already Installed';
                installBtn.disabled = true;
            }} else {{
                // Register service worker for PWA functionality
                if ('serviceWorker' in navigator) {{
                    navigator.serviceWorker.register('/sw.js')
                        .then(() => showStatus('🔧 App is ready for installation', 'success'))
                        .catch(() => showStatus('⚠️ Service Worker registration failed', 'warning'));
                }} else {{
                    showStatus('⚠️ PWA not fully supported on this browser', 'warning');
                }}
            }}

            // Detect iOS for specific instructions
            const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
            if (isIOS) {{
                showStatus('📱 iOS detected - Use Safari for best installation experience', 'warning');
            }}
        </script>
    </body>
    </html>
    """

@app.route('/projects')
def projects():
    """Projects listing page"""
    projects_html = ""
    for project in SAMPLE_PROJECTS:
        status_color = {
            'Completed': '#28a745',
            'In Progress': '#ffc107', 
            'Quoted': '#17a2b8'
        }.get(project['status'], '#6c757d')
        
        projects_html += f"""
        <div class="project-card">
            <h3>{project['project_name']}</h3>
            <div class="project-details">
                <p><strong>Client:</strong> {project['client_name']}</p>
                <p><strong>Status:</strong> <span style="color: {status_color}; font-weight: bold;">{project['status']}</span></p>
                <p><strong>Quote Value:</strong> ${project['quote_value']:,.2f}</p>
                <p><strong>Timeline:</strong> {project['start_date']} → {project['completion_date']}</p>
            </div>
        </div>
        """
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>REMC Projects</title>
        <meta name="theme-color" content="#1a472a">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #1a472a, #2d5a3d);
                color: white;
                margin: 0;
                padding: 20px;
                min-height: 100vh;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }}
            h1 {{ color: #ffd700; margin-bottom: 15px; font-size: 2.5em; }}
            .nav-links a {{
                color: #ffd700;
                text-decoration: none;
                padding: 12px 25px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                margin: 0 10px;
                font-weight: bold;
                display: inline-block;
                transition: all 0.3s ease;
            }}
            .nav-links a:hover {{
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
            }}
            .stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}
            .stat-card {{
                background: rgba(255, 255, 255, 0.1);
                padding: 25px;
                border-radius: 12px;
                text-align: center;
                backdrop-filter: blur(10px);
            }}
            .stat-number {{
                font-size: 2.5em;
                font-weight: bold;
                color: #ffd700;
                margin-bottom: 10px;
            }}
            .project-card {{
                background: rgba(255, 255, 255, 0.1);
                margin: 20px 0;
                padding: 25px;
                border-radius: 12px;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
            }}
            .project-card:hover {{
                background: rgba(255, 255, 255, 0.15);
                transform: translateY(-3px);
            }}
            .project-card h3 {{
                color: #ffd700;
                margin: 0 0 15px 0;
                font-size: 1.4em;
            }}
            .project-details p {{
                margin: 8px 0;
                font-size: 1.05em;
            }}
            .project-details strong {{
                color: #e0e0e0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📋 REMC Projects</h1>
                <div class="nav-links">
                    <a href="/">🏠 Home</a>
                    <a href="/install">📱 Install App</a>
                </div>
            </div>
            
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{len(SAMPLE_PROJECTS)}</div>
                    <div>Total Projects</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${sum(p['quote_value'] for p in SAMPLE_PROJECTS):,.0f}</div>
                    <div>Total Value</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len([p for p in SAMPLE_PROJECTS if p['status'] == 'In Progress'])}</div>
                    <div>Active Projects</div>
                </div>
            </div>
            
            <div class="projects-list">
                {projects_html}
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/manifest.json')
def manifest():
    """PWA Manifest for app installation"""
    return jsonify({
        "name": "REMC Project Management",
        "short_name": "REMC",
        "description": "REMC Project Management System - Construction & Earthmoving",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#1a472a",
        "theme_color": "#1a472a",
        "orientation": "portrait-primary",
        "scope": "/",
        "categories": ["business", "productivity"],
        "icons": [
            {
                "src": "/icon-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/icon-512x512.png", 
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ],
        "share_target": {
            "action": "/share",
            "method": "POST",
            "enctype": "multipart/form-data",
            "params": {
                "title": "title",
                "text": "text", 
                "url": "url",
                "files": [
                    {
                        "name": "files",
                        "accept": ["image/*", ".pdf", ".doc", ".docx"]
                    }
                ]
            }
        }
    })

@app.route('/sw.js')
def service_worker():
    """Service Worker for PWA functionality"""
    return f"""
    const CACHE_NAME = 'remc-v1';
    const urlsToCache = [
        '/',
        '/projects',
        '/install',
        '/manifest.json'
    ];

    self.addEventListener('install', function(event) {{
        event.waitUntil(
            caches.open(CACHE_NAME)
                .then(function(cache) {{
                    return cache.addAll(urlsToCache);
                }})
        );
    }});

    self.addEventListener('fetch', function(event) {{
        event.respondWith(
            caches.match(event.request)
                .then(function(response) {{
                    if (response) {{
                        return response;
                    }}
                    return fetch(event.request);
                }})
        );
    }});

    self.addEventListener('activate', function(event) {{
        event.waitUntil(
            caches.keys().then(function(cacheNames) {{
                return Promise.all(
                    cacheNames.map(function(cacheName) {{
                        if (cacheName !== CACHE_NAME) {{
                            return caches.delete(cacheName);
                        }}
                    }})
                );
            }})
        );
    }});
    """, 200, {'Content-Type': 'application/javascript'}

@app.route('/icon-192x192.png')
def icon_192():
    """192x192 PNG icon fallback"""
    # Return a simple SVG as PNG fallback
    svg_icon = f"""
    <svg width="192" height="192" xmlns="http://www.w3.org/2000/svg">
        <rect width="192" height="192" fill="#1a472a" rx="25"/>
        <text x="96" y="120" font-family="Arial" font-size="80" fill="#ffd700" text-anchor="middle">🏗️</text>
        <text x="96" y="160" font-family="Arial" font-size="24" fill="#ffd700" text-anchor="middle" font-weight="bold">REMC</text>
    </svg>
    """, 200, {'Content-Type': 'image/svg+xml'}
    return svg_icon

@app.route('/icon-512x512.png')
def icon_512():
    """512x512 PNG icon fallback"""
    svg_icon = f"""
    <svg width="512" height="512" xmlns="http://www.w3.org/2000/svg">
        <rect width="512" height="512" fill="#1a472a" rx="60"/>
        <text x="256" y="300" font-family="Arial" font-size="200" fill="#ffd700" text-anchor="middle">🏗️</text>
        <text x="256" y="420" font-family="Arial" font-size="60" fill="#ffd700" text-anchor="middle" font-weight="bold">REMC</text>
    </svg>
    """, 200, {'Content-Type': 'image/svg+xml'}
    return svg_icon

@app.route('/api/projects')
def api_projects():
    """API endpoint for projects data"""
    return jsonify(SAMPLE_PROJECTS)

if __name__ == '__main__':
    print("🚀 Starting REMC Web Application...")
    port = int(os.environ.get('PORT', 5000))
    print(f"🌍 Running on port: {port}")
    print(f"📱 Access from any device at:")
    print(f"   - Local: http://localhost:{port}")
    print(f"   - Install: http://localhost:{port}/install")
    print(f"   - Projects: http://localhost:{port}/projects")
    print("✅ For mobile installation, use the /install URL")
    
    app.run(host='0.0.0.0', port=port, debug=False)