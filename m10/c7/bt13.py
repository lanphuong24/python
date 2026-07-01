## Toán 10 - Tiêu điểm và đường chuẩn của parabol
# Parabol dạng chính tắc: y^2 = 2px  (p > 0)

# Chương trình nhận vào:
#   p (p > 0)
# Trả về:
#   Tọa độ tiêu điểm F và phương trình đường chuẩn
# VD: p=2   => F(1.0;0), x=-1.0
#     p=6   => F(3.0;0), x=-3.0
# Gợi ý:
#   Tiêu điểm: F(p/2 ; 0)
#   Đường chuẩn: x = -p/2

def tieu_diem_duong_chuan(p):
    return f" F({p/2};0), x={-p/2}"


p = float(input("Nhập p: "))
print(tieu_diem_duong_chuan(p))
