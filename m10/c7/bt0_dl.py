## Toán 10 - Tính độ lớn của vector

# Chương trình nhận vào:
#   Vector u(a;b)
# Gợi ý: import math, dùng math.sqrt()
# VD: u(3;4)   => 5.0
#     u(1;0)   => 1.0
#     u(1;1)   => 1.41

import math

def vec_do_lon(ab):
    return math.sqrt((ab[0])**2 + (ab[1])**2)


a, b = map(int, input("Nhập vector u(a;b): ").split())
print(vec_do_lon([a, b]))
