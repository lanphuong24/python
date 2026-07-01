## Toán 10 - Tạo vector từ 2 điểm

# Chương trình nhận vào:
#   Điểm A(x1;y1) và điểm B(x2;y2)
# Trả về vector AB dưới dạng list [a, b]
# VD: A(1;2),  B(4;6)   => [3, 4]
#     A(0;0),  B(3;-1)  => [3, -1]
#     A(2;3),  B(1;1)   => [-1, -2]

def vec_AB(A, B):
    return [B[0]-A[0], B[1]-A[1]]


x1, y1 = map(int, input("Nhập điểm A(x1;y1): ").split())
x2, y2 = map(int, input("Nhập điểm B(x2;y2): ").split())
print(vec_AB([x1, y1], [x2, y2]))
