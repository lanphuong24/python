## Toán 10 - Lập phương trình đường thẳng từ vector chỉ phương và điểm cho trước

# Chương trình nhận vào:
#   Vector chỉ phương v(a;b) và điểm A(x0;y0)
# Trả về chuỗi dạng "ax + by + c = 0"
# VD: v(1;2),  A(3;1)   => "-2x + y + 5 = 0"
#     v(2;1),  A(0;-1)  => "-x + 2y + 2 = 0"
#     v(1;0),  A(2;3)   => "y - 3 = 0"

def vec_pt_tu_vcpt(v, A):
    a = -v[1]
    b = v[0]
    c = -a*A[0]-b*A[1]
    return f"{a}x + {b}y + {c} = 0"

a, b = map(int, input("Nhập vector chỉ phương v(a;b): ").split())
x0, y0 = map(int, input("Nhập tọa độ A(x0;y0): ").split())
print(vec_pt_tu_vcpt([a, b], [x0, y0]))
