## Tính tổng dãy số 1^3 + 2^3 + 3^3 + ... n^3

# Nhập số nguyên n.
# Tính tổng dãy số.

n = int(input('Nhap so nguyen n: '))
tong = 0
for i in range(1,n+1):
    tong = tong + i**3
print(tong)