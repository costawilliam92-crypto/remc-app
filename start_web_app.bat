@echo off
echo Starting REMC Web Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or later
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "..\\.venv" (
    echo Error: Virtual environment not found
    echo Please run this from the REMC project directory
    pause
    exit /b 1
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment...
call "..\\.venv\\Scripts\\activate.bat"

echo Installing web dependencies...
pip install -r requirements.txt

REM Get network IP for sharing
echo.
echo Getting network information...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    set "ip=%%a"
    goto :found
)
:found
set "ip=%ip: =%"

echo.
echo ========================================
echo REMC Web Application Starting...
echo ========================================
echo.
echo Access the application from:
echo   Local:    http://localhost:5000
echo   Network:  http://%ip%:5000
echo.
echo For iOS devices, use the network address
echo Add to home screen for app-like experience
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Start the web application
python app.py

pause