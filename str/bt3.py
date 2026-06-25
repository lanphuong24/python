## Thao tác cơ bản trên xâu ký tự

s = "banana"
c = "a"

# Đếm xem ký tự c xuất hiện bao nhiêu lần trong xâu s
# Code phải đảm bảo vẫn đúng khi sửa đổi s và c

i = 0
times = 0
while i < len(s):
    if s[i] == c:
      times += 1
    i += 1

print(f"Ký tự '{c}' xuất hiện {times} lần trong '{s}'")

# Trong python có hỗ trợ sẵn hàm đếm ký tự không?
