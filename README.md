# w01-backend-health-api
1. Hướng dẫn chạy Local
Để khởi chạy server ở môi trường local, bạn thực hiện theo các bước sau:

Đảm bảo máy đã cài đặt Python 3.

Kích hoạt môi trường ảo (virtual environment) của dự án.

Mở Git Bash tại thư mục gốc và chạy lệnh:

python server.py
2. Thông tin API Endpoint
Sau khi server khởi chạy thành công, endpoint cục bộ sẽ sẵn sàng tiếp nhận yêu cầu:

URL: http://localhost:8000/api/health

Phương thức (Method): GET

Phản hồi chuẩn (Response): 200 OK kèm dữ liệu định dạng JSON.

3. Quy trình kiểm thử (Testing với Postman)
Toàn bộ các test case phục vụ việc kiểm thử tự động đã được cấu hình sẵn trong dự án:

Biến môi trường: Sử dụng biến {{baseUrl}} (đảm bảo đã cấu hình giá trị http://localhost:8000 tại environment Local).

Đường dẫn lưu trữ: Bộ thư mục Collection được đặt tên là Intern Training, bạn có thể import vào Postman từ đường dẫn:

docs/postman/Intern Training.postman_collection.json