## Toán 10 - Lập phương trình tham số từ vector chỉ phương
# và điểm cho trước

# Chương trình nhận vào:
#   Vector chỉ phương v(a;b) và điểm A(x0;y0)
# Trả về chuỗi gồm 2 phương trình tham số:
#   x = x0 + a*t
#   y = y0 + b*t
# VD: v(2;1),  A(3;-2) => "x = 3 + 2t & y = -2 + t"
#     v(1;-3), A(0;4)  => "x = t & y = 4 - 3t"
#     v(-2;5), A(1;0)  => "x = 1 - 2t & y = 5t"

pass

a, b = map(int, input("Nhập vector chỉ phương v(a;b): ").split())
x0, y0 = map(int, input("Nhập tọa độ A(x0;y0): ").split())
print(vec_pt_tham_so([a, b], [x0, y0]))
