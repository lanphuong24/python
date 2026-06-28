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

def dien_tich_tam_giac(A, B, C):
    pass


Ax, Ay = map(float, input("Nhập tọa độ A (x;y): ").split())
Bx, By = map(float, input("Nhập tọa độ B (x;y): ").split())
Cx, Cy = map(float, input("Nhập tọa độ C (x;y): ").split())
print(dien_tich_tam_giac([Ax, Ay], [Bx, By], [Cx, Cy]))
