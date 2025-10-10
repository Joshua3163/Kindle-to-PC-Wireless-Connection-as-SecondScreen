# Contributing to Screen Mirror Server

Thank you for your interest in contributing to Screen Mirror Server! We welcome contributions from the community and are grateful for your help in making this project better.

## 🤝 How to Contribute

### Reporting Bugs

1. **Check existing issues** first to avoid duplicates
2. **Use the bug report template** when creating a new issue
3. **Include detailed information**:
   - Operating system and version
   - Python version (if running from source)
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggesting Features

1. **Check existing feature requests** to avoid duplicates
2. **Use the feature request template** when creating a new issue
3. **Provide clear use cases** and explain why the feature would be valuable
4. **Consider implementation complexity** and compatibility

### Code Contributions

#### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/screen-mirror-server.git
   cd screen-mirror-server
   ```
3. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-number
   ```

#### Development Setup

1. **Install Python 3.8 or later**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```
3. **Run the application**:
   ```bash
   python mirror_server.py
   ```

#### Code Standards

- **Follow PEP 8** Python style guidelines
- **Use meaningful variable and function names**
- **Add comments** for complex logic
- **Write docstrings** for functions and classes
- **Keep functions small** and focused on a single task

#### Testing

- **Test your changes** thoroughly before submitting
- **Test on different screen resolutions** if UI-related
- **Test network connectivity** scenarios
- **Verify the executable build** works:
  ```bash
  python build_app.py
  ```

#### Commit Guidelines

- **Use clear, descriptive commit messages**
- **Start with a verb** in the imperative mood (e.g., "Add", "Fix", "Update")
- **Reference issue numbers** when applicable
- **Keep commits focused** on a single change

Examples:
```
Add multi-monitor selection feature (#15)
Fix rotation bug causing double transformation
Update README with new installation instructions
```

#### Pull Request Process

1. **Update documentation** if necessary
2. **Ensure all tests pass** and the app builds successfully
3. **Update the README** if you're adding new features
4. **Create a pull request** with:
   - Clear title and description
   - Reference to related issues
   - Screenshots for UI changes
   - Testing instructions

5. **Respond to feedback** promptly and make requested changes

## 📋 Development Guidelines

### Code Organization

```
screen-mirror-server/
├── mirror_server.py      # Main application
├── mirrorindex.html      # Web client
├── build_app.py         # Build script
├── requirements.txt     # Dependencies
├── docs/               # Documentation
├── .github/            # GitHub templates
└── dist/              # Built executables
```

### Architecture

- **`mirror_server.py`** - Main server application with WebSocket handling
- **`mirrorindex.html`** - Client-side web interface
- **`build_app.py`** - PyInstaller configuration and build automation

### Key Components

1. **Screen Capture** - Uses PIL/Pillow for screen grabbing
2. **WebSocket Server** - Real-time communication with clients
3. **HTTP Server** - Serves the web interface
4. **Network Detection** - Automatic IP and port management

## 🐛 Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## 📝 Documentation

When contributing, please update documentation as needed:

- **README.md** - Main project documentation
- **Code comments** - Inline documentation
- **Docstrings** - Function and class documentation

## 🚀 Release Process

Releases follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR** - Incompatible API changes
- **MINOR** - New functionality (backwards compatible)
- **PATCH** - Bug fixes (backwards compatible)

## 🤔 Questions?

If you have questions about contributing:

1. **Check the documentation** first
2. **Search existing issues** for similar questions
3. **Create a new issue** with the "question" label
4. **Be specific** about what you're trying to do

## 📞 Community

- **GitHub Issues** - Bug reports and feature requests
- **Pull Requests** - Code contributions and discussion
- **Discussions** - General questions and ideas

## 🙏 Recognition

Contributors will be:
- **Listed in the README** (for significant contributions)
- **Mentioned in release notes**
- **Credited in commit history**

Thank you for helping make Screen Mirror Server better for everyone! 🎉