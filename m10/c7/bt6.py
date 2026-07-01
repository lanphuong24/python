## Toán 10 - Vị trí của điểm so với đường tròn
# Đường tròn tâm I(a;b), bán kính R
# Điểm M(x;y) thuộc đường tròn khi IM = R, tức là (x-a)^2 + (y-b)^2 = R^2

# Chương trình nhận vào:
#   Tọa độ tâm I(a;b) và bán kính R
#   Tọa độ điểm M(x;y)
# Trả về:
#   "Trên đường tròn" nếu M nằm trên đường tròn
#   "Trong đường tròn" nếu M nằm trong đường tròn
#   "Ngoài đường tròn" nếu M nằm ngoài đường tròn
# VD: I(0;0), R=5, M(3;4)   => Trên đường tròn
#     I(0;0), R=5, M(1;1)   => Trong đường tròn
#     I(0;0), R=5, M(5;5)   => Ngoài đường tròn
import math

def kiem_tra_diem_duong_tron(I, R, M):
    IM = [M[0]-I[0], M[1]-I[1]]
    dthang = math.sqrt(IM[0]**2 + IM[1]**2)
    if dthang == R:
        return "trong duong tron"
    elif dthang > R:
        return "ngoai duong tron"
    else:
        return "trong duong tron"


a, b = map(float, input("Nhập tọa độ tâm I (a;b): ").split())
R = float(input("Nhập bán kính R: "))
x, y = map(float, input("Nhập tọa độ điểm M (x;y): ").split())
print(kiem_tra_diem_duong_tron([a, b], R, [x, y]))
