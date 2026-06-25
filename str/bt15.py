## Xâu chứa các chữ số

s = "3 1 4 1 5 9 2 6"

# Tính tổng các chữ số trong xâu s
# Gợi ý: dùng split() để tách, int() để chuyển sang số
# Code phải đảm bảo vẫn đúng khi sửa đổi xâu s

so = s.split()

total = 0
for i in so:
    total += int(i)

print("Xâu:", s)
print("Tổng:", total)
