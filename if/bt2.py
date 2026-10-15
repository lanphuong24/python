## Kiểm tra đăng nhập

# Nhập tên đăng nhập và mật khẩu
# Kiểm tra thông tin đăng nhập (so với thông tin đã có trong hệ thống)

username = "phuong"
password = "Phuong1234"

u = input('Nhap username: ')
p = input('Nhap password: ')
if u == username and p == password:
    print('Dang nhap thanh cong')
else:
    print('Dang nhap khong thanh cong')