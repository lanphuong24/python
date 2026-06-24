## Thao tác cơ bản trên danh sách

a = [8, 5, -10, 4, 8, -4]

# Xoá các số âm khỏi danh sách trên
# Code phải đảm bảo vẫn đúng khi sửa đổi danh sách a

print("Danh sách cũ:", a)

for i in range(len(a)):
    if a[i] < 0:
        a.remove(a[i])

print("Danh sách mới:", a)