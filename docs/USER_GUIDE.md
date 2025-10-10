# � User Guide - Kindle PC Mirror

Welcome to the complete user guide for Kindle PC Mirror! Transform your Kindle into the perfect eye-strain-free secondary screen for document editing, reading, and productivity work.

## 📖 Table of Contents

1. [Why Kindle as Secondary Screen?](#why-kindle-as-secondary-screen)
2. [Getting Started](#getting-started)
3. [Kindle Setup Guide](#kindle-setup-guide)
4. [Installation Methods](#installation-methods)
5. [Connecting Your Kindle](#connecting-your-kindle)
6. [Optimizing for E-ink Displays](#optimizing-for-e-ink-displays)
7. [Document Workflows](#document-workflows)
8. [Advanced Features](#advanced-features)
9. [Performance Optimization](#performance-optimization)
10. [Troubleshooting](#troubleshooting)
11. [Tips and Tricks](#tips-and-tricks)

## 📖 Why Kindle as Secondary Screen?

### 🎯 **Perfect for Digital Work**
Your Kindle isn't just for reading books! It's the ideal secondary display for:
- **📝 Document editing** without eye strain
- **📚 Research and reference** materials
- **💼 Long work sessions** without fatigue
- **☀️ Outdoor work** in bright sunlight
- **🔋 All-day productivity** with incredible battery life

### 👁️ **Health Benefits**
- **Zero blue light emission** from e-ink displays
- **No screen flicker** that causes eye fatigue
- **Perfect for extended reading** sessions
- **Reduces computer vision syndrome**
- **Ideal for people with light sensitivity**

### 💡 **Productivity Advantages**
- **Distraction-free** environment without notifications
- **Always-on display** that doesn't drain battery
- **Portable** and lightweight for any workspace
- **Silent operation** perfect for libraries or quiet spaces
- **Cost-effective** secondary screen solution

## 🚀 Getting Started

Kindle PC Mirror allows you to wirelessly display your PC screen on your Kindle e-reader, creating the perfect eye-strain-free secondary display for document work, reading, and productivity tasks.

### What You Need
- A Windows PC (Windows 10 or later recommended)
- A Kindle with WiFi capability and Experimental Browser
- Both devices on the same network connection
- Documents, PDFs, or text-based work to display

### How It Works
1. The app creates a local web server on your PC
2. Your Kindle connects to this server through its built-in browser
3. Your screen (or selected portions) stream to your Kindle in real-time
4. Optimized refresh rates and quality settings for e-ink displays

## 📖 Kindle Setup Guide

### Compatible Kindle Models
**Fully Tested:**
- Kindle Paperwhite (all generations with browser)
- Kindle Oasis (all generations)
- Kindle Scribe (excellent for document editing)

**Should Work:**
- Kindle Voyage
- Basic Kindle (with browser support)
- Older Kindle models with Experimental Browser

### Enable Kindle Web Browser
1. **Turn on your Kindle** and ensure it's connected to WiFi
2. **Go to Settings** (tap the gear icon)
3. **Navigate to:** Device Options → Advanced Options
4. **Find "Experimental Browser"** and enable it if not already active
5. **Note**: Some newer Kindles call it just "Browser" instead of "Experimental Browser"

### Network Setup
1. **Ensure** your Kindle and PC are on the same WiFi network
2. **Check** your WiFi settings on both devices
3. **For best results**, use a 2.4GHz network (better range and stability)

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

## � Connecting Your Kindle

### Step-by-Step Kindle Connection

1. **Start Kindle PC Mirror** on your computer
2. **Note the connection URL** displayed in the app window
   - Example: `http://192.168.1.100:8000`
3. **On your Kindle**: Tap the browser icon (or go to Experimental Browser)
4. **Clear the address bar** and type the full URL
5. **Navigate** to the page (may take 10-15 seconds to load)
6. **Tap "Connect"** button on the webpage
7. **Wait** for the initial image to appear (first load can take 30 seconds)
8. **Enjoy** your eye-strain-free secondary display!

### Kindle-Specific Tips
- **First connection** always takes longer - be patient!
- **Tap refresh** in browser if connection seems stuck
- **Use landscape mode** on Kindle for wider documents
- **Portrait mode** is perfect for reading documents and PDFs
- **Bookmark the page** for quick access later

### Optimizing Connection Quality
1. **Start with these settings:**
   - Quality: 80% (for crisp text)
   - Resolution: 1.0x (full detail)
   - FPS: 2-3 (perfect for e-ink refresh rate)
   - Rotation: 90° (portrait) for documents

2. **If connection is slow:**
   - Reduce quality to 60%
   - Try resolution scale of 0.8x
   - Lower FPS to 1-2

## 🔧 Optimizing for E-ink Displays

### Perfect Settings for Kindle
```
Quality: 70-90% (crisp text without overloading)
Resolution Scale: 0.8-1.0x (full detail for reading)
FPS: 1-3 (matches e-ink refresh capabilities)
Rotation: 90° for documents, 0° for wide content
```

### E-ink Display Considerations
- **Refresh Rate**: E-ink displays refresh slowly (1-2 seconds)
- **Contrast**: High contrast works better than subtle grays
- **Text Size**: Larger text displays better on e-ink
- **Scrolling**: Slow, deliberate scrolling works best
- **Colors**: E-ink shows only black, white, and grays

### Document Display Optimization
1. **Word Documents**: Use large fonts (14pt+) and high contrast themes
2. **PDFs**: Zoom to comfortable reading size before mirroring
3. **Web Pages**: Use reader mode or high contrast extensions
4. **Code Editors**: Use high contrast themes with large fonts
5. **Spreadsheets**: Zoom to show fewer columns but larger text

## 📝 Document Workflows

### Writing and Editing Workflow
1. **Setup**: Open your document on PC, mirror to Kindle
2. **Position**: Place Kindle beside your keyboard for easy reference
3. **Work**: Edit on PC while reading current section on Kindle
4. **Benefits**: No need to scroll up/down constantly, reduced eye strain

### Research Workflow
1. **Research Window**: Open research materials/PDFs on one monitor
2. **Mirror to Kindle**: Display research content on Kindle
3. **Write**: Use main monitor for writing while referencing Kindle
4. **Advantages**: Keep references visible while writing, no window switching

### Document Review Workflow
1. **Full Document**: Display entire document on Kindle for overview
2. **Section Focus**: Show specific sections while editing on PC
3. **Track Changes**: View document with comments/changes on Kindle
4. **Proofreading**: Read entire document on eye-friendly Kindle display

### Presentation Workflow
1. **Teleprompter**: Display presentation notes on Kindle
2. **Speaker Notes**: Keep talking points visible during video calls
3. **Reference**: Show key data/charts during presentations
4. **Portable**: Take Kindle anywhere for reference material

### Coding Workflow
1. **Documentation**: Keep API docs or references on Kindle
2. **Code Review**: Display code files for review on Kindle
3. **Terminal Output**: Monitor logs or output on secondary screen
4. **Testing**: Keep test cases or requirements visible

## 🎮 Using the Controls

### PC Server Controls

#### Kindle-Optimized Settings
- **Quality Slider**: 70-90% (optimized for text clarity)
- **Resolution Scale**: 0.8-1.0x (full detail for reading)
- **FPS Control**: 1-3 frames per second (perfect for e-ink)
- **Rotation**: 90° for portrait documents, 0° for landscape

#### Display Options
- **Monitor Selection**: Choose which monitor to share
- **Rotation**: Perfect orientation for different document types
- **Area Selection**: Mirror specific windows or screen regions

#### Network Settings
- **Auto IP Detection**: Automatically finds your network IP
- **Port Settings**: Uses ports 8000 and 8765 (usually automatic)
- **Connection Status**: Shows connected Kindle devices

### Kindle/Device Controls

#### On the Kindle Browser
- **🔄 Rotate Button**: Cycle through rotation angles
- **📺 Monitor Button**: Switch between monitors (if multiple available)
- **⛶ Fullscreen Button**: Enter fullscreen mode
- **🔄 Refresh**: Reload connection if needed

#### Kindle Navigation
- **Tap to navigate**: Use touchscreen to interact with browser
- **Zoom**: Pinch gesture on touchscreen Kindles
- **Page turn buttons**: Can be used for browser navigation on some models
- **Menu button**: Access browser menu and bookmarks

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