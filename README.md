# 📱 Screen Mirror Server

[![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.0.0-red.svg)](https://github.com/ugurfeyzullah/screen-mirror-server/releases)

> **Mirror your PC screen to any device with a web browser - no apps required!**

A lightweight, easy-to-use application that allows you to wirelessly mirror your Windows PC screen to any device (phone, tablet, laptop) through a web browser. Perfect for presentations, monitoring, gaming, or just viewing your desktop from anywhere on your local network.

![Screen Mirror Demo](docs/demo-preview.png)

## ✨ Features

### 🚀 **Core Functionality**
- **📺 Real-time screen mirroring** - View your PC screen on any device
- **🌐 Browser-based client** - No apps needed on viewing devices
- **🔄 Rotation controls** - 0°, 90°, 180°, 270° rotation options
- **⚙️ Quality settings** - Adjustable compression (10-95%)
- **📏 Resolution scaling** - 0.1x to 1.0x scaling for performance
- **🎮 FPS control** - 1-30 frames per second

### 🛠️ **Technical Features**
- **🔍 Automatic network detection** - Smart IP and port management
- **🔧 Built-in diagnostics** - Connection testing and troubleshooting
- **📱 Mobile-optimized interface** - Touch-friendly controls
- **⛶ Fullscreen support** - Immersive viewing experience
- **🖥️ Multi-monitor support** - Choose which screen to share
- **� Local network only** - No internet required, secure by default

## 🚀 Quick Start

### Download & Run (Recommended)
1. **[Download the latest release](https://github.com/ugurfeyzullah/screen-mirror-server/releases)**
2. **Extract** `ScreenMirrorServer_v1.0.zip`
3. **Run** `ScreenMirrorServer.exe`
4. **Connect** from your phone using the displayed URL

### System Installation
1. **Extract** all files from the zip
2. **Right-click** `install.bat` → "Run as Administrator"
3. **Launch** from Start Menu or Desktop shortcut

## � How to Connect

1. **Start** Screen Mirror Server on your PC
2. **Note** the connection URL (e.g., `http://192.168.1.100:8000`)
3. **Open** any browser on your phone/tablet
4. **Enter** the URL and click "Connect"
5. **Enjoy** wireless screen mirroring!

## �️ System Requirements

- **OS:** Windows 10 or later (Windows 7/8 may work)
- **Network:** WiFi or Ethernet connection
- **RAM:** 100MB minimum
- **Storage:** 50MB disk space
- **Ports:** 8000, 8765 (automatically managed)

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
git clone https://github.com/ugurfeyzullah/screen-mirror-server.git
cd screen-mirror-server

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

The application supports various configuration options:

```python
# Quality Settings
quality = 50          # Image quality (10-95%)
resolution_scale = 1.0 # Resolution scaling (0.1-1.0)
fps = 10              # Frames per second (1-30)

# Network Settings
http_port = 8000      # HTTP server port
websocket_port = 8765 # WebSocket server port
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

## � Bug Reports & Feature Requests

- **🐛 Found a bug?** [Open an issue](https://github.com/ugurfeyzullah/screen-mirror-server/issues/new?template=bug_report.md)
- **💡 Have an idea?** [Request a feature](https://github.com/ugurfeyzullah/screen-mirror-server/issues/new?template=feature_request.md)

## 📊 Statistics

![GitHub stars](https://img.shields.io/github/stars/ugurfeyzullah/screen-mirror-server?style=social)
![GitHub forks](https://img.shields.io/github/forks/ugurfeyzullah/screen-mirror-server?style=social)
![GitHub issues](https://img.shields.io/github/issues/ugurfeyzullah/screen-mirror-server)
![GitHub downloads](https://img.shields.io/github/downloads/ugurfeyzullah/screen-mirror-server/total)

## � Acknowledgments

- **[Pillow](https://python-pillow.org/)** - Image processing
- **[websockets](https://websockets.readthedocs.io/)** - WebSocket implementation
- **[PyInstaller](https://pyinstaller.org/)** - Executable packaging

## 📧 Contact

- **Author:** Ugur Feyzullah
- **GitHub:** [@ugurfeyzullah](https://github.com/ugurfeyzullah)
- **Project Link:** [https://github.com/ugurfeyzullah/screen-mirror-server](https://github.com/ugurfeyzullah/screen-mirror-server)

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ for wireless screen sharing

</div>