## Tính tổng dãy số 1 + 1/2 + 1/3 + ... + 1/n

# Nhập số nguyên n.
# Tính tổng dãy số.

n = int(input("nhap so nguyen: "))
t = 0
for i in range(1,n + 1):
    t = t + 1 / i
print("tong day so:", t)