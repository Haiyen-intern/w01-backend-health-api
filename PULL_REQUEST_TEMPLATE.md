## Ý nghĩa của PR 
- Khởi tạo môi trường Backend đơn giản bằng thư viện `http.server` và cấu hình môi trường ảo (`venv`).
- Tạo API endpoint `/api/health` trả về kết quả JSON trạng thái hệ thống.

## Kết quả kiểm thử dưới Local & Cấu hình
- [x] Đã khởi chạy server thành công tại cổng 8000 trong môi trường ảo.
- [x] Test qua Postman sử dụng biến môi trường `{{baseUrl}}` trả về mã 200 OK và JSON đúng cấu trúc.
- [x] Đã lưu response example và export Collection vào đúng thư mục `docs/postman/`.
- [x] Cấu hình file `.gitignore` để loại bỏ các file rác của Postman tự sinh dưới máy.