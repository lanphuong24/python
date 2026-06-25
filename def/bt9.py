## Định nghĩa hàm

# Viết hàm giai_ptb2 nhận vào 3 hệ số a, b, c
# Giải phương trình bậc 2: ax² + bx + c = 0
# Trả về list chứa các nghiệm của phương trình
# vd: giai_ptb2(1, -5, 6) => [3.0, 2.0]
#     giai_ptb2(1, 2, 1)  => [-1.0]
#     giai_ptb2(1, 1, 1)  => []
# Gợi ý: import math và dùng math.sqrt() để tính căn bậc 2

import math

def giai_ptb2(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return []
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        return [x1, x2]
    else:
        x = -b / 2 * a
        return [x]


print(giai_ptb2(1, -5, 6))    # [3.0, 2.0]
print(giai_ptb2(1, 2, 1))     # [-1.0]
print(giai_ptb2(1, 1, 1))     # []
