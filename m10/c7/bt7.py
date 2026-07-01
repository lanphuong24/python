## Toán 10 - Tìm giao điểm 2 đường thẳng
# d1: a1x + b1y + c1 = 0  và  d2: a2x + b2y + c2 = 0

# Chương trình nhận vào:
#   Hệ số của 2 đường thẳng dạng tổng quát
# Trả về:
#   Tọa độ giao điểm M(x;y) nếu 2 đường thẳng cắt nhau
#   List rỗng nếu 2 đường thẳng song song hoặc trùng nhau
# VD: d1(1;-1;0),  d2(1;1;-2)  => [1.0;1.0]
#     d1(1;-2;3),  d2(2;1;-4)  => [1.0;2.0]
#     d1(1;-1;0),  d2(2;-2;1)  => []
#     d1(1;-1;0),  d2(2;-2;0)  => []
# Gợi ý: Giải hệ phương trình bằng định thức (quy tắc Cramer)
#   D  = a1*b2 - a2*b1
#   Dx = -c1*b2 + c2*b1
#   Dy = -a2*c1 + a1*c2
#   Nếu D == 0: trả về []
#   Nếu D != 0: x = Dx/D, y = Dy/D

def giao_diem_2_duong_thang(d1, d2):
    a1 = d1[0]
    b1 = d1[1]
    c1 = d1[2]
    a2 = d2[0]
    b2 = d2[1]
    c2 = d2[2]
    D  = a1*b2 - a2*b1
    Dx = -c1*b2 + c2*b1
    Dy = -a1*c2 + a2*c1
    if D == 0:
        return []
    else:
        return [Dx/D, Dy/D]
    


a1, b1, c1 = map(int, input("Nhập hệ số d1 (a1;b1;c1): ").split())
a2, b2, c2 = map(int, input("Nhập hệ số d2 (a2;b2;c2): ").split())
print(giao_diem_2_duong_thang([a1, b1, c1], [a2, b2, c2]))
