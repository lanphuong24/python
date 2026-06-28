## Toán 10 - Phương trình tiếp tuyến của đường tròn
# Đường tròn tâm I(a;b), bán kính R
# Tiếp tuyến tại điểm M(x0;y0) thuộc đường tròn

# Chương trình nhận vào:
#   Tọa độ tâm I(a;b), bán kính R
#   Tọa độ điểm M(x0;y0)
# Trả về:
#   Phương trình tiếp tuyến dạng Ax + By + C = 0
# VD: I(0;0), R=5, M(3;4)    => 3x + 4y - 25 = 0
#     I(1;2), R=5, M(4;6)    => 3x + 4y - 36 = 0
# Gợi ý: Tiếp tuyến tại M vuông góc với bán kính IM tại M
#   Vectơ pháp tuyến của tiếp tuyến = vectơ IM = (x0-a ; y0-b)
#   Phương trình: (x0-a)(x - x0) + (y0-b)(y - y0) = 0

def tiep_tuyen_duong_tron(I, R, M):
    pass


a, b = map(float, input("Nhập tọa độ tâm I (a;b): ").split())
R = float(input("Nhập bán kính R: "))
x0, y0 = map(float, input("Nhập tọa độ điểm M (x0;y0): ").split())
print(tiep_tuyen_duong_tron([a, b], R, [x0, y0]))
