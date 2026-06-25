## Định nghĩa hàm

# Viết hàm count_char nhận vào xâu s và ký tự c
# Trả về số lần ký tự c xuất hiện trong s
# vd: count_char("banana", "a") => 3

def count_char(s, c):
    dem = 0
    for i in s:
        if i == c:
            dem += 1
    return dem


print(count_char("banana", "a"))   # 3
print(count_char("hello", "l"))    # 2
print(count_char("python", "x"))   # 0

# Trong python xâu có hỗ trợ sẵn hàm đếm ký tự không?
