@echo off
echo Installing Screen Mirror Server...
echo.

:: Create installation directory
set INSTALL_DIR=%PROGRAMFILES%\ScreenMirrorServer
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Copy executable
copy "ScreenMirrorServer.exe" "%INSTALL_DIR%\"

:: Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Screen Mirror Server.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\\ScreenMirrorServer.exe'; $Shortcut.Save()"

:: Create start menu shortcut
set START_MENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs
if not exist "%START_MENU%\Screen Mirror Server" mkdir "%START_MENU%\Screen Mirror Server"
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%START_MENU%\\Screen Mirror Server\\Screen Mirror Server.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\\ScreenMirrorServer.exe'; $Shortcut.Save()"

echo.
echo Installation complete!
echo Desktop shortcut created
echo Start menu shortcut created
echo.
pause
