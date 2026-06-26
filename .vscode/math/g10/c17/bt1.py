## Toán 10 - Lập phương trình đường thẳng từ vector pháp tuyến 
# và điểm cho trước

# Chương trình nhận vào:
#   VTPT u(a;b) và điểm A(x0;y0)
# Trả về chuỗi dạng "ax + by + c = 0"
# Công thức: a(x-x0) + b(y-y0)=0
# VD: u(2;3), A(1;-1)  => "2x + 3y + 1 = 0"
#     u(1;-2), A(3;4)  => "x - 2y + 5 = 0"
#     u(3;0),  A(2;5)  => "3x - 6 = 0"

pass

a, b = map(int, input("Nhập VTPT u(a;b): ").split())
x0, y0 = map(int, input("Nhập tọa độ A(x0;y0): ").split())
print(pt_duong_thang(a, b, x0, y0))
