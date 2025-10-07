# REMC Web Application

A web-based version of the REMC project management system that works on iOS, Android, and desktop devices.

## Features

- **Cross-Platform**: Works on any device with a web browser
- **iOS Compatible**: Optimized for iOS Safari with touch-friendly interface
- **Responsive Design**: Adapts to different screen sizes
- **Project Management**: View and search all projects
- **Email Tracking**: View tracked emails with attachments
- **Real-time Data**: Access to live project and email data

## Getting Started

### Prerequisites

- Python 3.8 or later
- REMC desktop application data files

### Installation

1. Ensure the main REMC application is set up in the parent directory
2. Run `start_web_app.bat` to start the web server
3. Open the provided URL in your web browser

### For iOS Devices

1. Open Safari and navigate to the network URL (e.g., http://192.168.x.x:5000)
2. Tap the Share button in Safari
3. Select "Add to Home Screen"
4. The app will now appear as an icon on your home screen
5. Launch it for a full-screen, app-like experience

## Usage

### Dashboard
- Overview of project statistics
- Quick search functionality
- Recent projects display

### Projects
- Browse all residential and commercial projects
- Search by name, ID, client, or location
- Switch between list and grid views
- View detailed project information

### Email Tracking
- View all tracked emails
- Filter by project, date, or content
- View email attachments and details
- Navigate to associated projects

## Mobile Optimization

The application is specifically optimized for mobile devices:

- Touch-friendly interface
- Responsive design that adapts to screen size
- Mobile-specific navigation patterns
- Optimized loading for mobile networks
- Support for iOS Safari and Android Chrome

## Technical Details

- **Framework**: Flask (Python web framework)
- **Frontend**: Bootstrap 5 + custom CSS
- **Data Source**: Existing REMC JSON data files
- **Compatibility**: Modern web browsers
- **Network**: Accessible on local network for device sharing

## File Structure

```
REMC_Web/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── start_web_app.bat  # Windows startup script
├── templates/         # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── projects.html
│   ├── project_detail.html
│   ├── emails.html
│   ├── help.html
│   └── settings.html
└── static/           # Static files (CSS, JS, images)
```

## Network Access

The web application runs on your local network, making it accessible from any device connected to the same Wi-Fi network. This is perfect for:

- Using on iOS/Android devices
- Sharing with team members
- Remote access within the office
- Tablet-friendly project management

## Support

For help and troubleshooting:
- Access the built-in Help page
- Check the Settings page for system information
- Ensure the desktop REMC application data is available

## Version

Version 1.0.0 - Initial web-based implementation