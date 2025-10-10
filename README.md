# � Kindle PC Mirror - Eye-Friendly Secondary Display

[![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.0.0-red.svg)](https://github.com/ugurfeyzullah/kindle-pc-mirror/releases)
[![E-ink](https://img.shields.io/badge/E--ink-Friendly-green.svg)]()

> **Transform your Kindle into an eye-friendly secondary screen for document editing and reading!**

A specialized application designed to mirror your PC screen to Kindle e-readers and other e-ink devices, creating the perfect eye-strain-free secondary display for reading and editing Word documents, PDFs, and text-based work. Also works with any touch-screen device through a web browser - no apps required!



Uploading test.mp4…



## 🎯 **Primary Use Case: Kindle as Secondary Screen**

**Perfect for digital nomads, writers, and anyone who spends hours reading/editing documents!**

### 📖 **Why Kindle + PC?**
- **👁️ Zero Eye Strain**: E-ink displays don't emit blue light or cause eye fatigue
- **📝 Document Editing**: Read Word docs, PDFs, and text files on your Kindle while editing on PC
- **⚡ Extended Work Sessions**: Work for hours without tired eyes
- **🔋 Battery Life**: Kindles last days/weeks, perfect for long work sessions
- **☀️ Outdoor Readable**: E-ink works perfectly in bright sunlight
- **💡 Distraction-Free**: Dedicated reading device without notifications

### 🎨 **Perfect Workflows**
- **📄 Document Review**: Display Word/PDF on Kindle while taking notes on PC
- **📚 Research**: Keep reference materials on Kindle while writing
- **💼 Presentations**: Use Kindle as teleprompter or presentation notes
- **📊 Data Analysis**: Display charts/data on Kindle while working in Excel
- **📖 E-book Creation**: Preview your writing in real e-book format

## ✨ Features

### � **Kindle & E-ink Optimized**
- **🖤 E-ink friendly**: Optimized refresh rates and contrast for e-ink displays
- **📱 Kindle browser support**: Works with Kindle's experimental web browser
- **🔄 Document rotation**: Perfect orientation for reading documents
- **⚙️ E-ink settings**: Specialized quality settings for e-paper displays
- **🔋 Battery efficient**: Minimal power consumption on e-readers

### �🚀 **Core Functionality**
- **📺 Real-time screen mirroring** - View your PC screen on Kindle or any device
- **🌐 Browser-based client** - No apps needed, works with any web browser
- **🔄 Rotation controls** - 0°, 90°, 180°, 270° rotation for perfect document viewing
- **⚙️ Quality settings** - Adjustable compression optimized for text readability
- **📏 Resolution scaling** - Perfect scaling for different screen sizes
- **🎮 Refresh rate control** - Optimized for e-ink display refresh capabilities

### 🛠️ **Technical Features**
- **🔍 Automatic network detection** - Smart IP and port management
- **🔧 Built-in diagnostics** - Connection testing and troubleshooting
- **📱 Touch-screen optimized** - Works on phones, tablets, and touch devices
- **⛶ Fullscreen support** - Immersive document viewing experience
- **🖥️ Multi-monitor support** - Choose which screen to mirror
- **🔒 Local network only** - No internet required, secure and private

## 🚀 Quick Start

### For Kindle Users (Primary Use Case)
1. **[Download the latest release](https://github.com/ugurfeyzullah/kindle-pc-mirror/releases)**
2. **Extract** `KindlePCMirror_v1.0.zip`
3. **Run** `KindlePCMirror.exe` on your PC
4. **On your Kindle**: Settings → Device Options → Advanced Options → Experimental Browser
5. **Connect** to the displayed URL (e.g., `http://192.168.1.100:8000`)
6. **Enjoy** eye-strain-free document viewing!

### For Other Touch Devices
1. **Download and run** the application
2. **Connect** from any device using the displayed URL
3. **Perfect for** tablets, phones, and other touch screens

### System Installation
1. **Extract** all files from the zip
2. **Right-click** `install.bat` → "Run as Administrator"
3. **Launch** from Start Menu or Desktop shortcut

## 📖 How to Connect Your Kindle

### Enable Kindle Web Browser
1. **Go to** Settings on your Kindle
2. **Navigate to** Device Options → Advanced Options
3. **Enable** "Experimental Browser" (if not already enabled)
4. **Connect** Kindle to the same WiFi as your PC

### Connect to PC
1. **Start** Kindle PC Mirror on your computer
2. **Note** the connection URL (e.g., `http://192.168.1.100:8000`)
3. **Open** Experimental Browser on your Kindle
4. **Enter** the URL in the address bar
5. **Click** "Connect" and start reading without eye strain!

### Optimize for E-ink
- **Set quality** to 70-90% for crisp text
- **Use portrait mode** (90° rotation) for documents
- **Adjust scaling** to fit your Kindle screen perfectly

## 🖥️ System Requirements

### For PC (Server)
- **OS:** Windows 10 or later
- **Network:** WiFi or Ethernet connection
- **RAM:** 100MB minimum
- **Storage:** 50MB disk space
- **Ports:** 8000, 8765 (automatically managed)

### For Kindle (Client)
- **Device:** Any Kindle with WiFi and Experimental Browser
- **Tested on:** Kindle Paperwhite, Kindle Oasis, Kindle Scribe
- **Network:** Same WiFi network as PC
- **Browser:** Experimental Browser (built-in)

### For Other Devices
- **Any device** with web browser support
- **Tablets:** iPad, Android tablets, Windows tablets
- **Phones:** iPhone, Android phones
- **Computers:** Mac, Linux, other Windows PCs

## 🛠️ Development Setup

### Prerequisites
```bash
# Python 3.8+ required
python --version

# Install required packages
pip install -r requirements.txt
```

### Running from Source
```bash
# Clone the repository
git clone https://github.com/ugurfeyzullah/kindle-pc-mirror.git
cd kindle-pc-mirror

# Install dependencies
pip install -r requirements.txt

# Run the application
python mirror_server.py
```

### Building Executable
```bash
# Quick build
python build_app.py

# Or use the batch script
build.bat

# The executable will be in the dist/ folder
```

## 📚 Documentation

- **[User Guide](docs/USER_GUIDE.md)** - Complete usage instructions
- **[Developer Guide](docs/DEVELOPER_GUIDE.md)** - Technical documentation
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[API Reference](docs/API.md)** - WebSocket protocol documentation

## 🔧 Configuration

### E-ink Optimized Settings
```python
# For Kindle and E-ink displays
quality = 80             # High quality for crisp text
resolution_scale = 1.0   # Full resolution for text clarity
fps = 2                  # Low refresh rate for e-ink
rotation = 90            # Portrait mode for documents

# For regular displays
quality = 50             # Balanced quality/performance
resolution_scale = 0.7   # Scaled for performance
fps = 15                 # Smooth refresh rate
```

### Network Settings
```python
http_port = 8000         # HTTP server port
websocket_port = 8765    # WebSocket server port
auto_ip_detection = True # Automatic network discovery
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

- **🐛 Found a bug?** [Open an issue](https://github.com/ugurfeyzullah/kindle-pc-mirror/issues/new?template=bug_report.md)
- **💡 Have an idea?** [Request a feature](https://github.com/ugurfeyzullah/kindle-pc-mirror/issues/new?template=feature_request.md)
- **📖 Kindle-specific issues?** Please mention your Kindle model and firmware version

## 📊 Statistics

![GitHub stars](https://img.shields.io/github/stars/ugurfeyzullah/kindle-pc-mirror?style=social)
![GitHub forks](https://img.shields.io/github/forks/ugurfeyzullah/kindle-pc-mirror?style=social)
![GitHub issues](https://img.shields.io/github/issues/ugurfeyzullah/kindle-pc-mirror)
![GitHub downloads](https://img.shields.io/github/downloads/ugurfeyzullah/kindle-pc-mirror/total)

## � Acknowledgments

- **[Pillow](https://python-pillow.org/)** - Image processing
- **[websockets](https://websockets.readthedocs.io/)** - WebSocket implementation
- **[PyInstaller](https://pyinstaller.org/)** - Executable packaging

## 📧 Contact

- **Author:** Ugur Feyzullah
- **GitHub:** [@ugurfeyzullah](https://github.com/ugurfeyzullah)
- **Project Link:** [https://github.com/ugurfeyzullah/kindle-pc-mirror](https://github.com/ugurfeyzullah/kindle-pc-mirror)

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ for eye-strain-free computing and Kindle enthusiasts

</div>
