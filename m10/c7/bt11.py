## Toán 10 - Tiêu điểm và tiêu cự của elip
# Elip dạng chuẩn: x^2/a^2 + y^2/b^2 = 1  (a > b > 0)

# Chương trình nhận vào:
#   a, b (với a > b > 0)
# Trả về:
#   Tọa độ 2 tiêu điểm F1, F2 và tiêu cự 2c
# VD: a=5, b=3   => F1(-4.0;0), F2(4.0;0), 2c=8.0
#     a=5, b=4   => F1(-3.0;0), F2(3.0;0), 2c=6.0
# Gợi ý:
#   c = sqrt(a^2 - b^2)
#   F1(-c;0), F2(c;0)
#   Tiêu cự = 2c

def tieu_diem_tieu_cu(a, b):
    pass


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(tieu_diem_tieu_cu(a, b))
