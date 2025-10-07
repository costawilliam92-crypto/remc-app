# REMC EARTHMOVING - Progressive Web App

A modern, native-like mobile application for REMC EARTHMOVING project management system.

## Features

- **Native App Experience**: Install on any device like a native app from app stores
- **Offline Functionality**: Works without internet connection using service workers
- **Business Division Support**: Separate dashboards for Commercial and Residential divisions
- **Real-time Project Management**: Live project tracking with progress indicators
- **Professional Design**: Custom REMC EARTHMOVING branding with responsive design
- **Cross-platform**: Works on iOS, Android, Windows, macOS, and web browsers

## Installation

### For Users
1. Visit the app URL on your mobile device
2. Look for "Add to Home Screen" or "Install App" prompt
3. Follow the installation instructions
4. Launch the app from your home screen like any native app

### For Deployment
1. Upload all files to Vercel, Netlify, or any static hosting service
2. Ensure HTTPS is enabled (required for PWA features)
3. Configure custom domain if desired
4. Share the URL with your team (60 users)

## Project Structure

```
REMC_VERCEL/
├── index.html          # Main PWA application
├── manifest.json       # PWA configuration and metadata
├── sw.js              # Service worker for offline functionality
├── icon-192x192.png   # App icon (192x192 pixels)
├── icon-512x512.png   # App icon (512x512 pixels)
└── README.md          # This file
```

## PWA Features

- **Installable**: Users can install the app on their devices
- **Responsive**: Optimized for mobile, tablet, and desktop
- **Offline Support**: Cached content available without internet
- **Push Notifications**: Ready for future notification features
- **Background Sync**: Sync data when connection is restored

## Business Divisions

### Commercial Division
- Large scale projects and earthmoving operations
- Commercial developments and infrastructure
- Highway and industrial projects
- Project values typically $500K+

### Residential Division
- Home improvements and residential earthworks
- Pool installations and foundation work
- Landscaping and subdivision preparation
- Project values typically under $200K

## Technologies Used

- **Progressive Web App (PWA)**: Modern web technologies for native app experience
- **Service Workers**: Offline functionality and caching
- **Web App Manifest**: Native installation and app metadata
- **Responsive CSS**: Mobile-first design approach
- **Vanilla JavaScript**: Lightweight and fast performance

## Browser Support

- Chrome/Edge: Full PWA support including installation
- Safari: Limited PWA support, add to home screen available
- Firefox: Service worker support, limited installation features
- Mobile browsers: Excellent support across iOS and Android

## Next Steps

1. **Deploy to Vercel**: Upload files for global hosting
2. **Add Custom Domain**: Configure professional URL
3. **Enable HTTPS**: Required for PWA installation features
4. **Test Installation**: Verify app installs correctly on various devices
5. **Roll out to Team**: Share with 60 users for testing and feedback

## Support

For technical support or customization requests, contact the development team.

---

**REMC EARTHMOVING** - Professional project management, anywhere, anytime.