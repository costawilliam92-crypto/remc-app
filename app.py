#!/usr/bin/env python3
"""
REMC Web Application
A web-based version of the REMC project management system
Compatible with iOS, Android, and desktop browsers
"""

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, session
import json
import os
import sys
from datetime import datetime, timedelta
import sqlite3
from werkzeug.utils import secure_filename
import hashlib
import secrets

# Add parent directory to path to import existing modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class REMCWebManager:
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    def load_projects(self):
        """Load all projects from JSON files"""
        projects = []
        
        # Load residential projects
        try:
            residential_file = os.path.join(self.base_dir, 'residential_data.json')
            if os.path.exists(residential_file):
                with open(residential_file, 'r') as f:
                    residential_data = json.load(f)
                    # Handle both list and dict formats
                    if isinstance(residential_data, dict):
                        for project_id, project in residential_data.items():
                            if isinstance(project, dict):
                                project['id'] = project_id
                                project['type'] = 'Residential'
                                projects.append(project)
                    elif isinstance(residential_data, list):
                        for i, project in enumerate(residential_data):
                            if isinstance(project, dict):
                                project['id'] = project.get('id', f'RES-{i+1}')
                                project['type'] = 'Residential'
                                projects.append(project)
        except Exception as e:
            print(f"Error loading residential data: {e}")
        
        # Load commercial projects
        try:
            app_data_file = os.path.join(self.base_dir, 'app_data.json')
            if os.path.exists(app_data_file):
                with open(app_data_file, 'r') as f:
                    app_data = json.load(f)
                    commercial_projects = app_data.get('projects', {})
                    for project_id, project in commercial_projects.items():
                        if isinstance(project, dict):
                            project['id'] = project_id
                            project['type'] = 'Commercial'
                            projects.append(project)
        except Exception as e:
            print(f"Error loading commercial data: {e}")
            
        return projects
    
    def load_email_tracking(self):
        """Load email tracking data"""
        try:
            email_file = os.path.join(self.base_dir, 'email_tracking.json')
            if os.path.exists(email_file):
                with open(email_file, 'r') as f:
                    data = json.load(f)
                    # Handle both list and dict formats
                    if isinstance(data, list):
                        # Convert list to dict with index as key
                        return {str(i): email for i, email in enumerate(data)}
                    return data
        except Exception as e:
            print(f"Error loading email tracking: {e}")
        return {}
    
    def get_project_stats(self):
        """Get dashboard statistics"""
        projects = self.load_projects()
        emails = self.load_email_tracking()
        
        stats = {
            'total_projects': len(projects),
            'active_projects': len([p for p in projects if p.get('status', '').lower() in ['active', 'in progress', 'ongoing']]),
            'completed_projects': len([p for p in projects if p.get('status', '').lower() in ['completed', 'finished']]),
            'total_emails': len(emails),
            'recent_emails': len([e for e in emails.values() if self._is_recent(e.get('received_time', ''))]),
            'residential_projects': len([p for p in projects if p.get('type') == 'Residential']),
            'commercial_projects': len([p for p in projects if p.get('type') == 'Commercial'])
        }
        return stats
    
    def _is_recent(self, date_str):
        """Check if date is within last 7 days"""
        try:
            if not date_str:
                return False
            # Handle different date formats
            for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y']:
                try:
                    date_obj = datetime.strptime(date_str, fmt)
                    return (datetime.now() - date_obj).days <= 7
                except ValueError:
                    continue
            return False
        except:
            return False
    
    def search_projects(self, query):
        """Search projects by name, ID, or description"""
        projects = self.load_projects()
        if not query:
            return projects
        
        query = query.lower()
        filtered = []
        
        for project in projects:
            # Search in project ID, name, description, client
            searchable_fields = [
                project.get('id', ''),
                project.get('name', ''),
                project.get('description', ''),
                project.get('client', ''),
                project.get('location', '')
            ]
            
            if any(query in str(field).lower() for field in searchable_fields):
                filtered.append(project)
        
        return filtered
    
    def get_project_emails(self, project_id):
        """Get all emails for a specific project"""
        emails = self.load_email_tracking()
        project_emails = []
        
        for email_id, email in emails.items():
            if email.get('tracked_project_id') == project_id:
                email['id'] = email_id
                project_emails.append(email)
        
        # Sort by received time (most recent first)
        project_emails.sort(key=lambda x: x.get('received_time', ''), reverse=True)
        return project_emails

# Initialize manager
remc_manager = REMCWebManager()

@app.route('/')
def index():
    """Main dashboard"""
    stats = remc_manager.get_project_stats()
    recent_projects = remc_manager.load_projects()[:5]  # Get first 5 projects
    return render_template('dashboard.html', stats=stats, recent_projects=recent_projects)

@app.route('/projects')
def projects():
    """Projects page with search"""
    search_query = request.args.get('search', '')
    projects_list = remc_manager.search_projects(search_query)
    return render_template('projects.html', projects=projects_list, search_query=search_query)

@app.route('/project/<project_id>')
def project_detail(project_id):
    """Project detail page with emails"""
    projects = remc_manager.load_projects()
    project = next((p for p in projects if p['id'] == project_id), None)
    
    if not project:
        return redirect(url_for('projects'))
    
    project_emails = remc_manager.get_project_emails(project_id)
    return render_template('project_detail.html', project=project, emails=project_emails)

@app.route('/emails')
def emails():
    """Email tracking page"""
    emails = remc_manager.load_email_tracking()
    email_list = []
    
    for email_id, email in emails.items():
        email['id'] = email_id
        email_list.append(email)
    
    # Sort by received time (most recent first)
    email_list.sort(key=lambda x: x.get('received_time', ''), reverse=True)
    
    return render_template('emails.html', emails=email_list)

@app.route('/api/projects/search')
def api_search_projects():
    """API endpoint for project search (for mobile autocomplete)"""
    query = request.args.get('q', '')
    projects = remc_manager.search_projects(query)
    
    # Return simplified project data for API
    simplified = []
    for project in projects[:10]:  # Limit to 10 results
        simplified.append({
            'id': project['id'],
            'name': project.get('name', ''),
            'type': project.get('type', ''),
            'client': project.get('client', ''),
            'status': project.get('status', '')
        })
    
    return jsonify(simplified)

@app.route('/api/stats')
def api_stats():
    """API endpoint for dashboard stats"""
    stats = remc_manager.get_project_stats()
    return jsonify(stats)

@app.route('/settings')
def settings():
    """Settings page"""
    return render_template('settings.html')

@app.route('/help')
def help_page():
    """Help page"""
    return render_template('help.html')

@app.route('/install')
def install_page():
    """App installation page"""
    return render_template('install.html')

@app.route('/share', methods=['GET', 'POST'])
def share_handler():
    """Handle shared content from PWA"""
    if request.method == 'POST':
        # Handle shared files/data
        title = request.form.get('title', '')
        text = request.form.get('text', '')
        url = request.form.get('url', '')
        files = request.files.getlist('files')
        
        # Process shared content (could save to projects)
        print(f"Shared content: title={title}, text={text}, url={url}")
        for file in files:
            print(f"Shared file: {file.filename}")
        
        # Redirect to main app
        return redirect(url_for('index'))
    
    # GET request - show share interface
    return render_template('share.html')

@app.route('/offline')
def offline_page():
    """Offline fallback page"""
    return render_template('offline.html')

@app.route('/static/manifest.json')
def manifest():
    """PWA Manifest"""
    response = send_file('static/manifest.json', mimetype='application/json')
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/static/sw.js')
def service_worker():
    """Service Worker"""
    response = send_file('static/sw.js', mimetype='application/javascript')
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/static/icon-192.svg')
def app_icon():
    """App Icon"""
    response = send_file('static/icon-192.svg', mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    return response

if __name__ == '__main__':
    # Get port from environment for Railway deployment
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # Run the web server
    print("Starting REMC Web Application...")
    print("Access from any device at:")
    print(f"- Local: http://localhost:{port}")
    print("- Network: http://192.168.0.46:5000")
    print("\nFor iOS devices, use the network address")
    print("For global access, use ngrok or Railway deployment")
    
    try:
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Error starting server: {e}")
        print("Press any key to exit...")
        input()