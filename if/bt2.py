## Kiểm tra đăng nhập

# Nhập tên đăng nhập và mật khẩu
# Kiểm tra thông tin đăng nhập (so với thông tin đã có trong hệ thống)

username = "phuong"
password = "Phuong1234"

user = input("nhap ten dang nhap: ")
pw = input("nhap mat khau: ")
if user == username and pw == password:
    print("dang nhap thanh cong")
else:
    print("dang nhap that bai")
