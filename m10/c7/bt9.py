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

import math

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

def duong_tron_ngoai_tiep(A, B, C):
    M = [(A[0]+B[0])/2, (A[1]+B[1])/2]
    a1 = B[0]-A[0]
    b1 = B[1]-A[1]
    c1 = -a1*M[0]-b1*M[1]

    N = [(A[0]+C[0])/2, (A[1]+C[1])/2]
    a2 = C[0]-A[0]
    b2 = C[1]-A[1]
    c2 = -a2*N[0]-b2*N[1]

    I = giao_diem_2_duong_thang([a1, b1, c1], [a2, b2, c2])

    vec_IA = [A[0]-I[0], A[1]-I[1]]
    ban_kinh = math.sqrt(vec_IA[0]**2 + vec_IA[1]**2)
    return f"(x - {I[0]})**2 + (y - {I[1]})**2 = {ban_kinh**2}"



Ax, Ay = map(float, input("Nhập tọa độ A (x;y): ").split())
Bx, By = map(float, input("Nhập tọa độ B (x;y): ").split())
Cx, Cy = map(float, input("Nhập tọa độ C (x;y): ").split())
print(duong_tron_ngoai_tiep([Ax, Ay], [Bx, By], [Cx, Cy]))
