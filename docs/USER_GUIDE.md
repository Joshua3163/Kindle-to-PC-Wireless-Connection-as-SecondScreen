# 📚 User Guide - Screen Mirror Server

Welcome to the complete user guide for Screen Mirror Server! This guide will walk you through everything you need to know to get the most out of your screen mirroring experience.

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [Installation Methods](#installation-methods)
3. [First Time Setup](#first-time-setup)
4. [Connecting Devices](#connecting-devices)
5. [Using the Controls](#using-the-controls)
6. [Advanced Features](#advanced-features)
7. [Performance Optimization](#performance-optimization)
8. [Troubleshooting](#troubleshooting)
9. [Tips and Tricks](#tips-and-tricks)

## 🚀 Getting Started

Screen Mirror Server allows you to wirelessly display your PC screen on any device with a web browser. No apps needed on your phone, tablet, or other devices!

### What You Need
- A Windows PC (Windows 10 or later recommended)
- A network connection (WiFi or Ethernet)
- Devices with web browsers to view the screen

### How It Works
1. The app creates a local web server on your PC
2. You connect to this server from any device on your network
3. Your screen is streamed in real-time through your web browser

## 💾 Installation Methods

### Method 1: Portable Executable (Easiest)
Perfect for quick use or trying out the app:

1. **Download** `ScreenMirrorServer.exe` from the releases
2. **Double-click** to run - no installation needed!
3. **Allow** Windows Firewall access when prompted

### Method 2: Full Installation (Recommended)
Best for regular use with desktop shortcuts and Start Menu integration:

1. **Download** the complete distribution package
2. **Extract** all files to a folder
3. **Right-click** `install.bat` and select "Run as Administrator"
4. **Follow** the installation prompts
5. **Find** the app in your Start Menu or Desktop

### Method 3: Run from Source (For Developers)
If you want to modify the code or contribute:

1. **Install** Python 3.8 or later
2. **Clone** the repository: `git clone https://github.com/ugurfeyzullah/screen-mirror-server.git`
3. **Install** dependencies: `pip install -r requirements.txt`
4. **Run** the app: `python mirror_server.py`

## 🔧 First Time Setup

### 1. Launch the Application
- **Installed version**: Find "Screen Mirror Server" in Start Menu
- **Portable version**: Double-click `ScreenMirrorServer.exe`
- **From source**: Run `python mirror_server.py`

### 2. Windows Firewall
When you first run the app, Windows will ask about firewall access:
- **Click "Allow access"** to enable network connections
- If you accidentally block it, you can fix this in Windows Defender Firewall settings

### 3. Check the Interface
The main window shows:
- **Connection URL**: The address for your devices to connect to
- **Status**: Whether the server is running
- **Controls**: Settings for quality, rotation, etc.

## 📱 Connecting Devices

### Step-by-Step Connection

1. **Start** Screen Mirror Server on your PC
2. **Look** for the connection URL in the app window
   - Example: `http://192.168.1.100:8000`
3. **Ensure** your device is on the same WiFi network as your PC
4. **Open** any web browser on your device (Chrome, Safari, Firefox, etc.)
5. **Type** the connection URL in the address bar
6. **Press** Enter and wait for the page to load
7. **Click** the "Connect" button on the webpage
8. **Enjoy** your mirrored screen!

### Connection Troubleshooting
If you can't connect:
- ✅ **Same Network**: Both devices must be on the same WiFi
- 🔥 **Firewall**: Temporarily disable Windows Firewall to test
- 🌐 **Test Locally**: First try the URL on your PC's browser
- 📱 **Try Different Browser**: Some browsers work better than others

## 🎮 Using the Controls

### PC Server Controls

#### Quality Settings
- **Quality Slider**: 10-95% - Lower = faster, Higher = clearer
- **Resolution Scale**: 0.1x to 1.0x - Lower = smaller image, faster
- **FPS Control**: 1-30 frames per second - Lower = less smooth, faster

#### Display Options
- **Rotation**: Choose 0°, 90°, 180°, or 270° rotation
- **Monitor Selection**: Choose which monitor to share (if you have multiple)

#### Network Settings
- **Auto IP Detection**: Automatically finds your network IP
- **Port Settings**: Uses ports 8000 and 8765 (usually automatic)

### Mobile/Device Controls

#### On the Webpage
- **🔄 Rotate Button**: Cycle through rotation angles (0°, 90°, 180°, 270°)
- **📺 Monitor Button**: Switch between monitors (if multiple available)
- **⛶ Fullscreen Button**: Enter fullscreen mode for immersive viewing

#### Touch Gestures
- **Pinch to Zoom**: Zoom in/out on the mirrored screen
- **Drag to Pan**: Move around when zoomed in
- **Double Tap**: Toggle fullscreen mode

## 🔧 Advanced Features

### Multi-Monitor Support
If you have multiple monitors:
1. **Select Monitor**: Use the monitor dropdown in the PC app
2. **Switch on Device**: Use the monitor button on the webpage
3. **Different Resolutions**: Each monitor can have different settings

### Performance Modes
For different use cases:

**Presentation Mode** (High Quality):
- Quality: 80-95%
- Resolution: 1.0x
- FPS: 15-20

**Gaming Mode** (Smooth):
- Quality: 30-50%
- Resolution: 0.5-0.7x
- FPS: 20-30

**Monitoring Mode** (Low Bandwidth):
- Quality: 20-40%
- Resolution: 0.3-0.5x
- FPS: 5-10

### Network Diagnostics
The app includes built-in diagnostics:
- **IP Detection**: Shows your network IP address
- **Port Testing**: Checks if ports are available
- **Connection Status**: Shows connected devices

## ⚡ Performance Optimization

### For Smooth Streaming
1. **Close Unnecessary Apps**: Free up CPU and memory
2. **Use Ethernet**: Wired connection is more stable than WiFi
3. **Reduce Quality**: Lower quality = better performance
4. **Optimize Network**: Use 5GHz WiFi if available

### For Best Quality
1. **High-End PC**: More powerful PC = better encoding
2. **Good Network**: Strong WiFi signal or wired connection
3. **Reduce Background**: Close other network-heavy apps
4. **Adjust Settings**: Find the sweet spot for your setup

### Battery Optimization (Mobile)
- **Lower Brightness**: Reduce phone screen brightness
- **Close Other Apps**: Free up mobile device resources
- **Use WiFi**: Don't use mobile data
- **Fullscreen Mode**: Reduces browser UI overhead

## 🔍 Troubleshooting

### Common Issues

#### "Can't Connect" Error
**Symptoms**: Browser shows "Can't reach this site"
**Solutions**:
1. Check both devices are on same WiFi
2. Verify the IP address is correct
3. Try disabling Windows Firewall temporarily
4. Restart the Screen Mirror Server

#### "Connection Lost" Error
**Symptoms**: Was working, but suddenly disconnected
**Solutions**:
1. Check WiFi connection on both devices
2. Restart the app and reconnect
3. Try different quality settings
4. Move closer to WiFi router

#### Poor Performance
**Symptoms**: Laggy, choppy, or slow video
**Solutions**:
1. Lower the quality setting (try 30-50%)
2. Reduce resolution scale (try 0.5x)
3. Lower FPS (try 10 FPS)
4. Close other apps on your PC

#### "Screen Not Updating"
**Symptoms**: Image is frozen or not refreshing
**Solutions**:
1. Click "Connect" again on the webpage
2. Refresh the browser page
3. Restart Screen Mirror Server
4. Check if PC is in sleep mode

### Advanced Troubleshooting

#### Network Issues
```bash
# Test network connectivity
ping 192.168.1.100  # Replace with your PC's IP

# Check if ports are available
netstat -an | findstr 8000
netstat -an | findstr 8765
```

#### Firewall Configuration
1. **Open** Windows Defender Firewall
2. **Click** "Allow an app or feature through Windows Defender Firewall"
3. **Find** "Screen Mirror Server" or "Python"
4. **Check** both Private and Public networks
5. **Click** OK

## 💡 Tips and Tricks

### Productivity Tips
- **Dual Monitor Setup**: Share one monitor while working on another
- **Remote Monitoring**: Check your PC status from anywhere in the house
- **Presentations**: Wireless presentations without cables or adapters

### Creative Uses
- **Gaming**: Stream gameplay to other devices
- **Video Playback**: Watch movies on your tablet using PC as source
- **Tutorials**: Show computer processes to others wirelessly

### Performance Tips
- **Restart Regularly**: Restart the app occasionally for best performance
- **Update Drivers**: Keep graphics drivers updated
- **Network Optimization**: Use QoS settings on your router if available

### Security Tips
- **Local Network Only**: App only works on local network (secure by default)
- **No Internet Required**: Everything stays on your home network
- **Temporary Access**: Server stops when app closes

## 🆘 Need More Help?

If this guide doesn't solve your issue:

1. **Check** the [Troubleshooting Guide](TROUBLESHOOTING.md)
2. **Search** existing [GitHub Issues](https://github.com/ugurfeyzullah/screen-mirror-server/issues)
3. **Create** a new issue with detailed information
4. **Include** your OS version, device types, and error messages

## 📧 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/ugurfeyzullah/screen-mirror-server/issues)
- **Documentation**: [Check other guides](../README.md)
- **Source Code**: [View on GitHub](https://github.com/ugurfeyzullah/screen-mirror-server)

---

**Happy screen mirroring! 🎉**