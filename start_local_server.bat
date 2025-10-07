@echo off
echo Starting REMC EARTHMOVING PWA Local Server...
echo.
echo This will start a local web server to test your PWA app
echo Open your browser to: http://localhost:8001
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
python -m http.server 8001