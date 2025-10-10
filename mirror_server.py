import asyncio
import websockets
import json
import tkinter as tk
from PIL import ImageGrab, Image
import io
import base64
import threading
import time
import socket
import http.server
import socketserver
import os
import webbrowser
import subprocess
import urllib.request
import urllib.error
import traceback
from tkinter import ttk

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, ws_port=None, **kwargs):
        self.ws_port = ws_port
        # Set the directory to the folder containing the mirrorindex.html
        if directory is None:
            directory = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, directory=directory, **kwargs)
    
    def log_message(self, format, *args):
        # Silence HTTP logs to avoid cluttering the console
        pass
        
    def do_GET(self):
        # Handle request to get the WebSocket port
        if self.path == '/get_ws_port':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
            self.send_header('Cache-Control', 'no-cache, no-store')  # Prevent caching
            self.end_headers()
            response = json.dumps({'ws_port': self.ws_port})
            print(f"Client requested WebSocket port. Sending: {self.ws_port}")
            self.wfile.write(response.encode('utf-8'))
            return
        
        # Serve the index page for root requests
        if self.path == '/' or self.path == '/index.html':
            self.path = '/mirrorindex.html'
        
        # Otherwise serve files as usual
        return super().do_GET()

class MirrorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Mirror Server")
        self.root.geometry("400x350")  # Made slightly taller for rotation controls
        
        # Create a frame for controls
        control_frame = tk.Frame(root, padx=10, pady=10)
        control_frame.pack(fill=tk.X)
        
        # Add rotation control
        rotation_frame = tk.Frame(control_frame)
        rotation_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(rotation_frame, text="Rotation:").pack(side=tk.LEFT)
        
        # Rotation variable and radio buttons
        self.rotation_var = tk.IntVar(value=0)
        rotations = [
            ("0°", 0),
            ("90°", 90),
            ("180°", 180),
            ("270°", 270)
        ]
        
        # Create radio buttons for each rotation option
        rotation_buttons_frame = tk.Frame(rotation_frame)
        rotation_buttons_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        for text, value in rotations:
            tk.Radiobutton(
                rotation_buttons_frame,
                text=text,
                variable=self.rotation_var,
                value=value
            ).pack(side=tk.LEFT, padx=10)
        
        # Quality slider
        quality_frame = tk.Frame(control_frame)
        quality_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(quality_frame, text="Image Quality:").pack(side=tk.LEFT)
        self.quality_var = tk.IntVar(value=50)
        quality_slider = ttk.Scale(quality_frame, from_=10, to=95, 
                                   variable=self.quality_var, orient=tk.HORIZONTAL)
        quality_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Label(quality_frame, textvariable=self.quality_var).pack(side=tk.LEFT, padx=5)
        
        # Resolution scaling slider
        scale_frame = tk.Frame(control_frame)
        scale_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(scale_frame, text="Resolution Scale:").pack(side=tk.LEFT)
        self.scale_var = tk.DoubleVar(value=1.0)
        scale_slider = ttk.Scale(scale_frame, from_=0.1, to=1.0, 
                                variable=self.scale_var, orient=tk.HORIZONTAL)
        scale_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Display the scale value with 1 decimal place
        self.scale_label = tk.Label(scale_frame, text="1.0")
        self.scale_label.pack(side=tk.LEFT, padx=5)
        
        # Update label when scale changes
        self.scale_var.trace_add("write", self.update_scale_label)
        
        # FPS control
        fps_frame = tk.Frame(control_frame)
        fps_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(fps_frame, text="FPS:").pack(side=tk.LEFT)
        self.fps_var = tk.IntVar(value=10)
        fps_slider = ttk.Scale(fps_frame, from_=1, to=30, 
                              variable=self.fps_var, orient=tk.HORIZONTAL)
        fps_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        tk.Label(fps_frame, textvariable=self.fps_var).pack(side=tk.LEFT, padx=5)
        
        # Add a test connection button
        test_frame = tk.Frame(control_frame)
        test_frame.pack(fill=tk.X, pady=5)
        
        self.test_btn = tk.Button(test_frame, text="Test Connection", 
                                 command=self.test_connection, bg="#2196F3", fg="white")
        self.test_btn.pack(side=tk.LEFT, padx=5)
        
        self.restart_btn = tk.Button(test_frame, text="Restart Servers", 
                                    command=self.restart_servers, bg="#FF9800", fg="white")
        self.restart_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label to show server state
        self.status_label = tk.Label(root, text="Starting servers...", font=("Arial", 12))
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        
        # Connection info
        self.conn_label = tk.Label(root, text="", font=("Arial", 10))
        self.conn_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Get local IP using improved method
        self.local_ip = self.get_local_ip()
        
        # This variable will hold the latest captured screen image as a base64 string.
        self.latest_image = None
        
        # Flag to control the screen capture loop.
        self.capturing = True
        
        # Server ports - find available ports for both
        self.http_port = self.find_available_port(8000)
        self.ws_port = self.find_available_port(8765)
        
        if self.http_port is None or self.ws_port is None:
            error_msg = "Error: Could not find available ports"
            print(error_msg)
            self.status_label.config(text=error_msg)
            return
        
        # Start HTTP server in a separate thread
        self.http_server_thread = threading.Thread(target=self.start_http_server)
        self.http_server_thread.daemon = True
        self.http_server_thread.start()
        
        # Start WebSocket server in a separate thread
        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.daemon = True
        self.server_thread.start()
        
        # Start screen capture loop in a separate thread
        self.capture_thread = threading.Thread(target=self.capture_loop)
        self.capture_thread.daemon = True
        self.capture_thread.start()
        
        # Open browser automatically
        self.open_browser_thread = threading.Thread(target=self.open_browser)
        self.open_browser_thread.daemon = True
        self.open_browser_thread.start()
        
        # Update connection info
        self.update_connection_info()
    
    def update_scale_label(self, *args):
        self.scale_label.config(text=f"{self.scale_var.get():.1f}")
    
    def get_local_ip(self):
        """Get the actual local IP address that can be reached from other devices."""
        try:
            # Connect to a remote address to determine which local interface to use
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                ip = s.getsockname()[0]
                print(f"Detected network IP: {ip}")
                return ip
        except Exception as e:
            print(f"Failed to detect network IP: {e}")
            # Fallback to the original method
            fallback_ip = socket.gethostbyname(socket.gethostname())
            print(f"Using fallback IP: {fallback_ip}")
            return fallback_ip
    
    def run_network_diagnostics(self):
        """Run basic network diagnostics to help troubleshoot connectivity."""
        try:
            # Test if we can bind to the IP and ports
            print(f"Testing HTTP port {self.http_port}...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((self.local_ip, self.http_port))
                print(f"✓ HTTP port {self.http_port} is accessible")
        except Exception as e:
            print(f"✗ HTTP port {self.http_port} test failed: {e}")
        
        try:
            print(f"Testing WebSocket port {self.ws_port}...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind((self.local_ip, self.ws_port))
                print(f"✓ WebSocket port {self.ws_port} is accessible")
        except Exception as e:
            print(f"✗ WebSocket port {self.ws_port} test failed: {e}")
        
        # Check for common network interfaces
        try:
            import subprocess
            result = subprocess.run(['ipconfig'], capture_output=True, text=True, timeout=5)
            if 'Wireless LAN adapter Wi-Fi' in result.stdout:
                print("✓ WiFi adapter detected")
            else:
                print("⚠ WiFi adapter not clearly detected")
        except Exception as e:
            print(f"Network interface check failed: {e}")
    
    def update_connection_info(self):
        # Create a message with both HTTP and WebSocket info
        info = f"Connect: http://{self.local_ip}:{self.http_port}/mirrorindex.html"
        self.conn_label.config(text=info)
        print("=" * 50)
        print("CONNECTION INFORMATION:")
        print(f"Server IP: {self.local_ip}")
        print(f"HTTP Port: {self.http_port}")
        print(f"WebSocket Port: {self.ws_port}")
        print(f"Full URL: {info}")
        print("\nNETWORK DIAGNOSTICS:")
        self.run_network_diagnostics()
        print("\nTROUBLESHOoting TIPS:")
        print("1. Make sure both devices are on the same WiFi network")
        print("2. Check Windows Firewall settings")
        print("3. Try accessing from PC browser first")
        print("4. Verify mirrorindex.html exists in the same folder")
        print("5. Try disabling Windows Firewall temporarily")
        print(f"6. Test connectivity: ping {self.local_ip} from your phone")
        print("=" * 50)
    
    def is_port_in_use(self, port):
        """Check if a port is already in use."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # Set SO_REUSEADDR to handle TIME_WAIT state
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(('0.0.0.0', port))
                return False
            except OSError as e:
                print(f"Port {port} is in use: {e}")
                return True
    
    def find_available_port(self, start_port, max_attempts=10):
        """Find an available port starting from start_port."""
        port = start_port
        for _ in range(max_attempts):
            if not self.is_port_in_use(port):
                return port
            port += 1
        
        # If we couldn't find an available port, return None and handle it later
        print(f"Warning: Could not find an available port after {max_attempts} attempts")
        return None
    
    def open_browser(self):
        # Wait a moment for servers to start
        time.sleep(1.5)
        url = f"http://{self.local_ip}:{self.http_port}/mirrorindex.html"
        try:
            webbrowser.open(url)
            print(f"Browser opened at {url}")
        except Exception as e:
            print(f"Failed to open browser: {e}")
    
    def update_status(self, message):
        self.root.after(0, lambda: self.status_label.config(text=message))
    
    def start_http_server(self):
        try:
            # Create a handler with access to the WebSocket port
            handler = lambda *args, **kwargs: CustomHTTPRequestHandler(
                *args, ws_port=self.ws_port, **kwargs
            )
            
            # Use SO_REUSEADDR to avoid "Address already in use" errors
            class ReuseAddrTCPServer(socketserver.TCPServer):
                allow_reuse_address = True
            
            with ReuseAddrTCPServer(("", self.http_port), handler) as httpd:
                print(f"HTTP server started at http://{self.local_ip}:{self.http_port}")
                print(f"WebSocket port is {self.ws_port}")
                self.update_status(f"HTTP: {self.local_ip}:{self.http_port}, WS: {self.ws_port}")
                self.update_connection_info()
                httpd.serve_forever()
        except Exception as e:
            error_msg = f"HTTP server error: {str(e)}"
            print(error_msg)
            self.update_status(error_msg)
    
    async def handler(self, websocket, path=None):
        client_addr = f"{websocket.remote_address[0]}:{websocket.remote_address[1]}"
        print(f"New client connected from: {client_addr}")
        self.update_status(f"Client connected: {client_addr}")
        try:
            while True:
                # If a new image is available, send it
                if self.latest_image:
                    message = json.dumps({
                        "type": "screen",
                        "image": self.latest_image,
                        "rotation": self.rotation_var.get()  # Send rotation info
                    })
                    await websocket.send(message)
                # Calculate sleep time based on FPS setting
                await asyncio.sleep(1 / self.fps_var.get())
        except websockets.exceptions.ConnectionClosed:
            print(f"Client {client_addr} disconnected")
            self.update_status("Client disconnected")
        except Exception as e:
            print(f"WebSocket error with client {client_addr}: {e}")
            self.update_status(f"WebSocket error: {str(e)}")
    
    def start_server(self):
        if self.ws_port is None:
            self.update_status("Error: Could not find an available WebSocket port")
            return
        
        async def run_websocket_server():
            """Async function to run the WebSocket server"""
            try:
                print(f"Starting WebSocket server on {self.local_ip}:{self.ws_port}")
                
                # Create a wrapper for the handler to make it compatible
                async def websocket_handler(websocket):
                    return await self.handler(websocket, None)
                
                server = await websockets.serve(websocket_handler, "0.0.0.0", self.ws_port)
                print(f"WebSocket server successfully started on {self.local_ip}:{self.ws_port}")
                await server.wait_closed()
            except Exception as e:
                error_msg = f"WebSocket server error: {str(e)}"
                print(error_msg)
                self.update_status(error_msg)
                traceback.print_exc()
        
        try:
            # Create a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            status_msg = f"Servers running - WebSocket: {self.local_ip}:{self.ws_port}, HTTP: {self.local_ip}:{self.http_port}"
            print(status_msg)
            self.update_status(status_msg)
            
            # Run the WebSocket server
            loop.run_until_complete(run_websocket_server())
        except Exception as e:
            error_msg = f"WebSocket server error: {str(e)}"
            print(error_msg)
            self.update_status(error_msg)
            traceback.print_exc()
    
    def capture_loop(self):
        while self.capturing:
            try:
                # Capture the current screen
                screenshot = ImageGrab.grab()
                
                # Apply resolution scaling if needed (but no rotation here)
                scale_factor = self.scale_var.get()
                if scale_factor < 1.0:
                    new_width = int(screenshot.width * scale_factor)
                    new_height = int(screenshot.height * scale_factor)
                    screenshot = screenshot.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                buffer = io.BytesIO()
                # Save the screenshot as JPEG with quality setting from slider
                screenshot.save(buffer, format="JPEG", quality=self.quality_var.get())
                img_bytes = buffer.getvalue()
                # Encode the image bytes as a base64 string
                self.latest_image = base64.b64encode(img_bytes).decode('utf-8')
                
                # Calculate sleep time to match desired FPS
                time.sleep(1 / self.fps_var.get())
            except Exception as e:
                print("Error capturing screen:", e)
                time.sleep(1)  # Wait a bit before retrying on error
    
    def test_connection(self):
        """Test if the server is accessible from the local network."""
        import urllib.request
        import urllib.error
        
        test_url = f"http://{self.local_ip}:{self.http_port}/get_ws_port"
        try:
            print(f"Testing connection to {test_url}...")
            response = urllib.request.urlopen(test_url, timeout=5)
            if response.getcode() == 200:
                print("✓ Server is accessible from local network")
                self.update_status("✓ Connection test successful")
            else:
                print(f"✗ Server returned status code: {response.getcode()}")
                self.update_status(f"✗ Test failed: HTTP {response.getcode()}")
        except urllib.error.URLError as e:
            print(f"✗ Connection test failed: {e}")
            self.update_status(f"✗ Connection test failed: {e}")
        except Exception as e:
            print(f"✗ Unexpected error during test: {e}")
            self.update_status(f"✗ Test error: {e}")
    
    def restart_servers(self):
        """Restart the servers (placeholder for now)."""
        print("To restart servers, please close and rerun the application.")
        self.update_status("Please restart the application to reset servers")

if __name__ == "__main__":
    root = tk.Tk()
    app = MirrorApp(root)
    root.mainloop()
