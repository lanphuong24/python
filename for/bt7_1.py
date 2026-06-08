## Tính tổng dãy số 1^3 + 2^3 + 3^3 + ... n^3

# Nhập số nguyên n.
# Tính tổng dãy số.

n = int(input("nhap so nguyen: "))
t = 0
for i in range(1, n + 1):
    t = t + i ** 3
print("tong day so", t)