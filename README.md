w01-backend-health-api
1. Hướng dẫn chạy Local
Để khởi chạy server ở môi trường local, bạn thực hiện theo các bước sau:

Bước 1: Đảm bảo máy đã cài đặt Python 3.

Bước 2: Mở Git Bash/Terminal tại thư mục gốc của dự án và kích hoạt môi trường ảo (virtual environment):

Đối với Windows (Git Bash / CMD):
.\venv\Scripts\activate

Đối với macOS / Linux:
source venv/bin/activate

Bước 3: Khởi chạy Backend server bằng lệnh:
python server.py

2. Thông tin API Endpoint
Sau khi server khởi chạy thành công, endpoint cục bộ sẽ sẵn sàng tiếp nhận yêu cầu:

URL: http://localhost:8000/api/health

Phương thức (Method): GET

Phản hồi chuẩn (Response): 200 OK kèm dữ liệu định dạng JSON mẫu như sau:

{
"status": "OK",
"message": "Backend server is running smoothly"
}

3. Quy trình kiểm thử (Testing với Postman)
Toàn bộ các test case phục vụ việc kiểm thử đã được cấu hình sẵn trong dự án:

Biến môi trường: Sử dụng biến {{baseUrl}} (đảm bảo bạn đã cấu hình giá trị http://localhost:8000 tại environment Local trên Postman).

Đường dẫn lưu trữ: Bộ thư mục Collection được đặt tên là Intern Training, bạn có thể import nhanh vào Postman từ đường dẫn: docs/postman/Intern Training.postman_collection.json
