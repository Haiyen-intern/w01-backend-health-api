import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. Define Request Handler
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the request matches the /api/health endpoint via GET method
        if self.path == '/api/health':
            # Send 200 OK success status code
            self.send_response(200)
            # Set response headers to application/json
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            # Define response payload
            response_data = {
                "status": "OK",
                "message": "Backend server is running smoothly",
                "environment": "local"
            }
            # Serialize JSON data and encode it to bytes before sending
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            # Return 404 Not Found error for invalid endpoints
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

# 2. Function to launch the HTTP Server on port 8000
def run(server_class=HTTPServer, handler_class=HealthCheckHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server is running at http://localhost:{port} ...")
    print("Press Ctrl + C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    run()