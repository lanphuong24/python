## Thao tác cơ bản trên danh sách

a = [8, 5, 10, 4, 8, 4]

# Tính tổng các số chẵn trong danh sách trên
# Code phải đảm bảo vẫn đúng khi sửa đổi danh sách a

total = 0
for e in a:
    if e % 2 == 0:
        total += e

print("Tổng cộng các số chẵn:", total)