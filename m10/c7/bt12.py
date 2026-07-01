## Toán 10 - Tiêu điểm và tiêu cự của hypebol
# Hypebol dạng chính tắc: x^2/a^2 - y^2/b^2 = 1

# Chương trình nhận vào:
#   a, b (a > 0, b > 0)
# Trả về:
#   Tọa độ 2 tiêu điểm F1, F2 và tiêu cự 2c
# VD: a=3, b=4    => F1(-5.0;0), F2(5.0;0), 2c=10.0
#     a=5, b=12   => F1(-13.0;0), F2(13.0;0), 2c=26.0
# Gợi ý:
#   c = sqrt(a^2 + b^2)
#   F1(-c;0), F2(c;0)
#   Tiêu cự = 2c

import math

def tieu_diem_tieu_cu_hypebol(a, b):
    c = math.sqrt(a**2 + b**2)
    return f" F1({-c};0), F2({c};0), 2c={2*c}"


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(tieu_diem_tieu_cu_hypebol(a, b))
