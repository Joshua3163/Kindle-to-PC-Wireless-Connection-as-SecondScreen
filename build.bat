@echo off
REM Quick build script for Screen Mirror Server
echo Building Screen Mirror Server...
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Build with PyInstaller
echo.
echo Building executable...
pyinstaller --clean mirror_server.spec

REM Check if build was successful
if exist "dist\ScreenMirrorServer.exe" (
    echo.
    echo ✓ Build successful!
    echo ✓ Executable created: dist\ScreenMirrorServer.exe
    echo.
    echo Creating installer...
    
    REM Create simple installer
    echo @echo off > dist\install.bat
    echo echo Installing Screen Mirror Server... >> dist\install.bat
    echo echo. >> dist\install.bat
    echo set INSTALL_DIR=%%PROGRAMFILES%%\ScreenMirrorServer >> dist\install.bat
    echo if not exist "%%INSTALL_DIR%%" mkdir "%%INSTALL_DIR%%" >> dist\install.bat
    echo copy "ScreenMirrorServer.exe" "%%INSTALL_DIR%%\\" >> dist\install.bat
    echo echo ✓ Installation complete! >> dist\install.bat
    echo pause >> dist\install.bat
    
    echo ✓ Installer created: dist\install.bat
    echo.
    echo 📁 Files ready for distribution:
    dir dist\*.exe dist\*.bat
    echo.
    echo 🎉 Ready to distribute!
) else (
    echo.
    echo ❌ Build failed!
    echo Check the error messages above.
)

pause