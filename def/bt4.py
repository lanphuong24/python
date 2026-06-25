## Định nghĩa hàm

# Viết hàm is_positive nhận vào một số, trả về True nếu số đó dương
# vd: is_positive(5)  => True
#     is_positive(-3) => False
#     is_positive(0)  => False

def is_positive(n):
    if n > 0:
        return True
    else:
        return False


print(is_positive(5))    # True
print(is_positive(-3))   # False
print(is_positive(0))    # False
