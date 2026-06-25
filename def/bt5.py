## Định nghĩa hàm

# Viết hàm min2 nhận vào 2 số, trả về số nhỏ hơn
# Không được dùng hàm min() có sẵn
# vd: min2(3, 7) => 3

def min2(a, b):
    if a < b:
        return a
    else:
        return b


print(min2(3, 7))    # 3
print(min2(10, 2))   # 2
print(min2(5, 5))    # 5
