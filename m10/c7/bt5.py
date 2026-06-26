## Toán 10 - Tính góc giữa 2 đường thẳng
# d1: a1x + b1y + c1 = 0  và  d2: a2x + b2y + c2 = 0

# Chương trình nhận vào:
#   Hệ số của 2 đường thẳng dạng tổng quát
# Trả về góc (độ) giữa 2 đường thẳng, làm tròn 2 chữ số thập phân
# Gợi ý: import math
#   math.acos(math.degrees(x)) chuyển đổi giá trị cos sang độ
#   math.fabs(x) tính trị tuyệt đối
# VD: d1(1;0;0),    d2(1;1;0)   => 45.0°
#     d1(1;0;0),    d2(0;1;0)   => 90.0°

pass

a1, b1, c1 = map(int, input("Nhập hệ số d1 (a1;b1;c1): ").split())
a2, b2, c2 = map(int, input("Nhập hệ số d2 (a2;b2;c2): ").split())
print(vec_goc_2_duong_thang([a1, b1, c1], [a2, b2, c2]))
