import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. Tạo Handler
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Kiểm tracó gọi đúng endpoint /api/health bằng phương thức GET không
        if self.path == '/api/health':
            #  200 OK (Thành công)
            self.send_response(200)
            # Khai báo dữ liệu
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            # Response
            response_data = {
                "status": "OK",
                "message": "Backend server is running smoothly",
                "environment": "local"
            }
            # Chuyển đổi dữ liệu
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            #  sai đường dẫn trả về lỗi 404 Not Found
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

# 2. Đoạn code để khởi chạy Server tại cổng 8000
def run(server_class=HTTPServer, handler_class=HealthCheckHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server đang chạy tại http://localhost:{port} ...")
    print("Nhấn Ctrl + C để dừng server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server đã dừng.")

if __name__ == '__main__':
    run()