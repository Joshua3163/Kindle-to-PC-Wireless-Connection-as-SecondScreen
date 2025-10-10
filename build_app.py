#!/usr/bin/env python3
"""
Build script to create a standalone executable for the Screen Mirror Server
"""

import subprocess
import sys
import os
import shutil

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")

def build_executable():
    """Build the executable using PyInstaller"""
    
    # Clean previous builds
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create a single executable file
        "--windowed",                   # Hide console window (remove this if you want console)
        "--name=ScreenMirrorServer",    # Name of the executable
        "--icon=icon.ico",              # Icon file (optional, create one if you want)
        "--add-data=mirrorindex.html;.", # Include the HTML file
        "--hidden-import=PIL",          # Ensure PIL is included
        "--hidden-import=websockets",   # Ensure websockets is included
        "--hidden-import=asyncio",      # Ensure asyncio is included
        "mirror_server.py"              # Main script
    ]
    
    # Remove icon parameter if icon file doesn't exist
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
        print("⚠ No icon.ico found, building without custom icon")
    
    try:
        print("Building executable...")
        print(f"Command: {' '.join(cmd)}")
        subprocess.check_call(cmd)
        print("✓ Executable built successfully!")
        print("📁 Check the 'dist' folder for your executable")
        
        # List the contents of dist folder
        if os.path.exists("dist"):
            print("\nFiles in dist folder:")
            for file in os.listdir("dist"):
                file_path = os.path.join("dist", file)
                size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
                print(f"  📄 {file} ({size:.1f} MB)")
                
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def create_installer_script():
    """Create a simple installer script"""
    installer_content = '''@echo off
echo Installing Screen Mirror Server...
echo.

:: Create installation directory
set INSTALL_DIR=%PROGRAMFILES%\\ScreenMirrorServer
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Copy executable
copy "ScreenMirrorServer.exe" "%INSTALL_DIR%\\"

:: Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Screen Mirror Server.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\\ScreenMirrorServer.exe'; $Shortcut.Save()"

:: Create start menu shortcut
set START_MENU=%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs
if not exist "%START_MENU%\\Screen Mirror Server" mkdir "%START_MENU%\\Screen Mirror Server"
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%START_MENU%\\Screen Mirror Server\\Screen Mirror Server.lnk'); $Shortcut.TargetPath = '%INSTALL_DIR%\\ScreenMirrorServer.exe'; $Shortcut.Save()"

echo.
echo ✓ Installation complete!
echo ✓ Desktop shortcut created
echo ✓ Start menu shortcut created
echo.
pause
'''
    
    with open("dist/install.bat", "w") as f:
        f.write(installer_content)
    
    print("✓ Installer script created: dist/install.bat")

def main():
    print("🔨 Building Screen Mirror Server Application")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("mirror_server.py"):
        print("❌ mirror_server.py not found in current directory")
        print("Please run this script from the same directory as mirror_server.py")
        return
    
    if not os.path.exists("mirrorindex.html"):
        print("❌ mirrorindex.html not found in current directory")
        print("Please ensure mirrorindex.html is in the same directory")
        return
    
    # Install PyInstaller if needed
    install_pyinstaller()
    
    # Build the executable
    if build_executable():
        # Create installer script
        create_installer_script()
        
        print("\n🎉 Build completed successfully!")
        print("\n📦 Distribution files:")
        print("  • ScreenMirrorServer.exe - Main executable")
        print("  • install.bat - Installer script")
        print("\n📋 Next steps:")
        print("  1. Test the executable by running dist/ScreenMirrorServer.exe")
        print("  2. Share the entire 'dist' folder with users")
        print("  3. Users can run install.bat to install the app system-wide")
        print("  4. Or users can run ScreenMirrorServer.exe directly")
    else:
        print("❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main()