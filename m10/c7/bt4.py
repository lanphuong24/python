## Toán 10 - Xác định vị trí tương đối giữa 2 đường thẳng
# d1: a1x + b1y + c1 = 0  và  d2: a2x + b2y + c2 = 0

# Chương trình nhận vào:
#   Hệ số của 2 đường thẳng dạng tổng quát
# Trả về chuỗi: "Cắt nhau", "Song song" hoặc "Trùng nhau"
# Gợi ý: so sánh tỉ lệ a1/a2, b1/b2, c1/c2 (dùng nhân chéo tránh chia)
# VD: d1(1;2;-3), d2(2;4;-6)  => "Trùng nhau"
#     d1(1;2;-3), d2(2;4;-8)  => "Song song"
#     d1(1;2;-3), d2(2;-1;1)  => "Cắt nhau"

pass

a1, b1, c1 = map(int, input("Nhập hệ số d1 (a1;b1;c1): ").split())
a2, b2, c2 = map(int, input("Nhập hệ số d2 (a2;b2;c2): ").split())
print(vec_vi_tri_tuong_doi([a1, b1, c1], [a2, b2, c2]))
