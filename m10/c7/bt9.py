## Toán 10 - Phương trình đường tròn ngoại tiếp tam giác
# Cho tam giác ABC, tìm tâm I và bán kính R của đường tròn ngoại tiếp

# Chương trình nhận vào:
#   Tọa độ 3 đỉnh A, B, C
# Trả về:
#   Chuỗi phương trình đường tròn dạng (x - a)^2 + (y - b)^2 = R^2
# VD: A(0;0), B(6;0), C(0;8)   => (x - 3.0)^2 + (y - 4.0)^2 = 25.0
#     A(1;1), B(5;1), C(1;4)   => (x - 3.0)^2 + (y - 2.5)^2 = 6.25
# Gợi ý:
#   Tìm đường thẳng 2 đường trung trực cắt AB và AC
#   Tìm giao điểm 2 đường trung trực vừa tìm được => tâm I
#   Bán kính R = IA
#   Định dạng phương trình đường tròn theo yêu cầu

def duong_tron_ngoai_tiep(A, B, C):
    pass


Ax, Ay = map(float, input("Nhập tọa độ A (x;y): ").split())
Bx, By = map(float, input("Nhập tọa độ B (x;y): ").split())
Cx, Cy = map(float, input("Nhập tọa độ C (x;y): ").split())
print(duong_tron_ngoai_tiep([Ax, Ay], [Bx, By], [Cx, Cy]))
