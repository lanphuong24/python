## Tính tổng dãy số 1 + 2 + 3 + ... + n

# Nhập số nguyên n
# Tính và in ra tổng dãy số từ 1 đến n

n = int(input("nhap so nguyen: "))
t = 0
for y in range(1, n + 1):
    t = t + y
print("tong:", t)