## Toán 10 - Tính độ lớn của vector

# Chương trình nhận vào:
#   Vector u(a;b)
# Gợi ý: import math, dùng math.sqrt()
# VD: u(3;4)   => 5.0
#     u(1;0)   => 1.0
#     u(1;1)   => 1.41

pass

a, b = map(int, input("Nhập vector u(a;b): ").split())
print(do_lon(a, b))
