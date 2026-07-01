## Toán 10 - Kiểm tra 2 vector có vuông góc không

# Chương trình nhận vào:
#   Vector u(a1;b1) và vector v(a2;b2)
# Trả về True nếu vuông góc, False nếu không
# VD: u(1;0),  v(0;1)   => True
#     u(1;1),  v(1;-1)  => True
#     u(1;2),  v(2;1)   => False

def vec_vuong_goc(a, b):
    return a[0] * a[1] + b[0] * b[1] == 0

a1, b1 = map(int, input("Nhập vector u(a1;b1): ").split())
a2, b2 = map(int, input("Nhập vector v(a2;b2): ").split())
print(vec_vuong_goc([a1, b1], [a2, b2]))
