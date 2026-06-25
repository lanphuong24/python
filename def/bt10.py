## Định nghĩa hàm - Hàm gọi hàm con

# Hàm is_nguyen_to đã được viết sẵn, dùng hàm con dem_uoc để kiểm tra số nguyên tố
# Viết hàm con dem_uoc(n) trả về số lượng ước của n
# vd: dem_uoc(6) => 4  (ước của 6 là: 1, 2, 3, 6)
#     dem_uoc(7) => 2  (ước của 7 là: 1, 7)

def dem_uoc(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    return dem


def is_nguyen_to(n):
    return dem_uoc(n) == 2


print(is_nguyen_to(7))    # True
print(is_nguyen_to(6))    # False
print(is_nguyen_to(1))    # False
print(is_nguyen_to(2))    # True
