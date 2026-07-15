What
Khởi tạo cấu trúc dự án Backend căn bản, cấu hình file .gitignore để lọc file rác (venv, __pycache__).
Tạo tài liệu hướng dẫn setup và khởi chạy môi trường local chi tiết trong file README.md.
Xây dựng thành công API endpoint GET /api/health trả về trạng thái hệ thống.
Cấu hình file PULL_REQUEST_TEMPLATE.md cho các phiên làm việc tiếp theo.
Khởi tạo và export Postman Collection phục vụ việc kiểm thử API.
Why
Cần có một cấu trúc dự án chuẩn và tài liệu hướng dẫn rõ ràng để các thành viên hoặc Mentor có thể dễ dàng setup và chạy thử dự án dưới local.
Tạo endpoint /api/health để kiểm tra độ ổn định, đảm bảo server có thể lắng nghe và phản hồi request một cách bình thường trước khi lên các framework lớn hơn (FastAPI/Django).
How
Sử dụng thư viện gốc http.server và json của Python để dựng HTTP Server đơn giản tại cổng 8000 mà không cần cài thêm thư viện ngoài.
Viết class HealthCheckHandler kế thừa từ BaseHTTPRequestHandler để bắt phương thức GET và trả về mã trạng thái 200 OK cùng header application/json.
Thiết lập quy trình Git Flow chuẩn: Tách nhánh feature/setup-backend-api từ main, commit theo chuẩn Conventional Commits và fix triệt để conflict trực tiếp dưới local trước khi gửi PR.