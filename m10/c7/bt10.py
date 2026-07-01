## Toán 10 - Tính diện tích tam giác
# Cho 3 đỉnh A, B, C

# Chương trình nhận vào:
#   Tọa độ 3 đỉnh A, B, C
# Trả về:
#   Diện tích tam giác ABC
# VD: A(0;0), B(4;0), C(0;3)   => 6.0
#     A(1;1), B(4;1), C(2;5)   => 6.0
# Gợi ý: S = 1/2 * đáy * đường cao
#   Lấy BC làm đáy: đáy = |BC|
#   Đường cao = khoảng cách từ A đến đường thẳng BC
#     Viết pt đường thẳng BC dạng tổng quát: ax + by + c = 0
#     h = |a*Ax + b*Ay + c| / sqrt(a^2 + b^2)

import math

def dien_tich_tam_giac(A, B, C):
    Vbc = [C[0]-B[0], C[1]-B[1]]
    day = math.sqrt(Vbc[0]**2 + Vbc[1]**2)
    Nbc = [-Vbc[1], Vbc[0]]
    a = Nbc[0]
    b = Nbc[1]
    c = -a*C[0] -b*C[1]
    cao = math.fabs(a*A[0] + b*A[1] + c) / math.sqrt(a**2 + b**2)
    return (day*cao)/2


Ax, Ay = map(float, input("Nhập tọa độ A (x;y): ").split())
Bx, By = map(float, input("Nhập tọa độ B (x;y): ").split())
Cx, Cy = map(float, input("Nhập tọa độ C (x;y): ").split())
print(dien_tich_tam_giac([Ax, Ay], [Bx, By], [Cx, Cy]))
