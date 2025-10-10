# 🔧 Troubleshooting Guide - Screen Mirror Server

Having trouble with Screen Mirror Server? This guide covers the most common issues and their solutions.

## 🚨 Quick Fixes

Try these first - they solve 80% of issues:

1. **🔄 Restart** the Screen Mirror Server app
2. **🌐 Refresh** the browser page on your device
3. **📶 Check** both devices are on the same WiFi network
4. **🔥 Temporarily disable** Windows Firewall
5. **📱 Try a different browser** on your device

## 📋 Connection Issues

### ❌ "Can't Connect to Server" / "Site Can't Be Reached"

**Symptoms:**
- Browser shows "This site can't be reached"
- "Connection timed out" error
- Page won't load at all

**Solutions:**

1. **Network Check:**
   ```
   ✅ Both devices on same WiFi network?
   ✅ PC connected to internet?
   ✅ Mobile device connected to WiFi (not mobile data)?
   ```

2. **IP Address Verification:**
   - Check the IP shown in Screen Mirror Server
   - Try typing the IP directly: `http://192.168.1.100:8000`
   - If IP is `127.0.0.1`, restart the app

3. **Firewall Fix:**
   - Temporarily disable Windows Defender Firewall
   - If it works, add Screen Mirror Server to firewall exceptions
   - **Steps:** Control Panel → System and Security → Windows Defender Firewall → Allow an app

4. **Port Issues:**
   - Close other programs that might use ports 8000 or 8765
   - Try restarting your PC if ports are stuck

5. **Router Settings:**
   - Some routers block device-to-device communication
   - Look for "AP Isolation" or "Client Isolation" - disable it
   - Try connecting both devices to router's 2.4GHz network

### ⚠️ "Connection Lost" / Frequent Disconnections

**Symptoms:**
- Connects but disconnects after a few seconds/minutes
- "WebSocket connection failed" errors
- Stream stops randomly

**Solutions:**

1. **WiFi Signal:**
   - Move closer to WiFi router
   - Check WiFi signal strength on both devices
   - Switch to 5GHz WiFi if available and both devices support it

2. **Power Settings:**
   - Disable "USB selective suspend" in Power Options
   - Set WiFi adapter to never turn off in Device Manager
   - Disable PC sleep mode while using the app

3. **Background Apps:**
   - Close other network-heavy applications
   - Disable Windows Updates during use
   - Close cloud sync applications (OneDrive, Dropbox, etc.)

4. **Performance Settings:**
   - Lower quality to 30-50%
   - Reduce FPS to 10-15
   - Try resolution scale of 0.5x

## 🐌 Performance Issues

### 📺 Laggy/Choppy Video

**Symptoms:**
- Video stutters or freezes
- Long delay between PC and device
- Very low frame rate

**Quick Fixes:**
```
Quality: 30-50% (instead of high quality)
FPS: 10-15 (instead of 30)
Resolution Scale: 0.5x (instead of 1.0x)
```

**Advanced Solutions:**

1. **PC Performance:**
   - Close unnecessary applications
   - Check Task Manager for high CPU/Memory usage
   - Update graphics drivers
   - Restart PC if it's been running for days

2. **Network Optimization:**
   - Use ethernet cable for PC if possible
   - Connect to 5GHz WiFi band
   - Move devices closer to router
   - Check for network interference (microwaves, baby monitors)

3. **Browser Optimization:**
   - Clear browser cache on mobile device
   - Close other browser tabs
   - Try different browsers (Chrome usually works best)
   - Enable hardware acceleration in browser settings

### 🖼️ Poor Image Quality

**Symptoms:**
- Blurry or pixelated image
- Colors look washed out
- Text is hard to read

**Solutions:**

1. **Quality Settings:**
   - Increase quality to 70-90%
   - Set resolution scale to 1.0x
   - Ensure you're not zoomed in on browser

2. **Monitor Settings:**
   - Check PC monitor resolution is optimal
   - Verify color settings on both PC and device
   - Try different rotation settings

3. **Network Bandwidth:**
   - Ensure good WiFi connection
   - Close streaming services on other devices
   - Try during off-peak hours

## 🔧 Technical Issues

### 💻 App Won't Start

**Symptoms:**
- Double-clicking does nothing
- Error messages on startup
- App crashes immediately

**Solutions:**

1. **Windows Compatibility:**
   - Right-click app → Properties → Compatibility
   - Try "Run as Administrator"
   - Try "Windows 8 compatibility mode"

2. **Missing Dependencies:**
   ```bash
   # If running from source:
   pip install --upgrade pillow websockets
   
   # For executable version:
   # Download fresh copy from GitHub releases
   ```

3. **Antivirus Issues:**
   - Check if antivirus is blocking the app
   - Add exception for Screen Mirror Server
   - Try disabling real-time protection temporarily

4. **File Permissions:**
   - Right-click app → Properties → Security
   - Ensure your user has "Full Control"
   - Try moving app to different folder (like Desktop)

### 🌐 WebSocket Errors

**Symptoms:**
- "WebSocket connection failed"
- "Error connecting to server"
- JavaScript console errors

**Solutions:**

1. **Browser Settings:**
   - Enable JavaScript in browser
   - Disable ad blockers for the site
   - Clear browser cache and cookies
   - Try incognito/private browsing mode

2. **Network Configuration:**
   - Check router firewall settings
   - Disable VPN on both devices
   - Try different WiFi network if available

3. **Port Conflicts:**
   ```bash
   # Check if ports are in use:
   netstat -an | findstr 8000
   netstat -an | findstr 8765
   
   # Close conflicting applications
   ```

## 📱 Device-Specific Issues

### 🍎 iOS/iPhone Issues

**Common Problems:**
- Safari blocks WebSocket connections
- Screen doesn't rotate properly
- Fullscreen doesn't work

**Solutions:**
- Use Chrome instead of Safari
- Enable "Allow Cross-Website Tracking" for the site
- Try adding to home screen as web app
- Update iOS to latest version

### 🤖 Android Issues

**Common Problems:**
- Chrome shows security warnings
- Battery optimization kills connection
- Screen rotation issues

**Solutions:**
- Allow "Insecure Content" for local IP
- Disable battery optimization for Chrome
- Enable "Auto-rotate screen" in Android settings
- Try Firefox if Chrome doesn't work

### 💻 Other Computer Issues

**Common Problems:**
- Corporate networks block connections
- Older browsers don't support WebSockets
- Proxy settings interfere

**Solutions:**
- Use personal hotspot instead of corporate WiFi
- Update browser to latest version
- Disable proxy settings temporarily
- Try different browser (Chrome, Firefox, Edge)

## 🔍 Advanced Diagnostics

### Network Testing

1. **Ping Test:**
   ```bash
   # From mobile device browser, visit:
   http://YOUR_PC_IP:8000/ping
   
   # Should show simple test page
   ```

2. **Port Test:**
   ```bash
   # On PC, open Command Prompt:
   netstat -an | findstr :8000
   netstat -an | findstr :8765
   
   # Should show LISTENING status
   ```

3. **IP Verification:**
   ```bash
   # On PC, open Command Prompt:
   ipconfig
   
   # Look for IPv4 Address under your network adapter
   ```

### Error Log Analysis

**Windows Event Viewer:**
1. Press Windows + R, type `eventvwr`
2. Navigate to Windows Logs → Application
3. Look for Screen Mirror Server errors

**Browser Developer Tools:**
1. Open webpage on device
2. Press F12 (or menu → Developer Tools)
3. Check Console tab for JavaScript errors

## 🆘 When All Else Fails

### Emergency Troubleshooting Steps

1. **Complete Reset:**
   - Uninstall and reinstall the app
   - Restart both PC and mobile device
   - Reset network adapter on PC
   - Forget and reconnect to WiFi on mobile device

2. **Alternative Connection Methods:**
   - Try mobile hotspot from phone
   - Use different WiFi network
   - Connect via Ethernet cable to PC

3. **System Information to Collect:**
   ```
   PC Information:
   - Windows version (Windows 10, 11)
   - Antivirus software
   - Network adapter type
   - IP address and network settings
   
   Mobile Device:
   - Device model and OS version
   - Browser type and version
   - WiFi connection details
   - Any error messages
   ```

### Getting Help

If you're still having issues:

1. **📝 Create a Bug Report:**
   - Go to [GitHub Issues](https://github.com/ugurfeyzullah/screen-mirror-server/issues)
   - Use the bug report template
   - Include all error messages and system information

2. **🔍 Search Existing Issues:**
   - Someone else might have had the same problem
   - Check closed issues for solutions

3. **💬 Ask for Help:**
   - Describe exactly what happens
   - Include steps you've already tried
   - Mention your device types and network setup

## 📊 Common Error Codes

| Error | Meaning | Solution |
|-------|---------|----------|
| Connection refused | Port is blocked | Check firewall settings |
| Timeout | Network issue | Check WiFi connection |
| WebSocket failed | Browser issue | Try different browser |
| 404 Not Found | Wrong URL | Verify IP address |
| 500 Server Error | App crashed | Restart the application |

## 🔧 Prevention Tips

**To avoid future issues:**

1. **Regular Maintenance:**
   - Restart the app weekly
   - Keep Windows updated
   - Update device browsers regularly

2. **Network Stability:**
   - Use quality WiFi router
   - Keep devices close to router
   - Avoid network congestion times

3. **Performance Optimization:**
   - Don't max out all settings at once
   - Find optimal settings for your network
   - Monitor network usage

---

**Still need help? [Create an issue](https://github.com/ugurfeyzullah/screen-mirror-server/issues) with detailed information!**