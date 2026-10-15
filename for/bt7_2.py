## Tính tổng dãy số 1 + 1/2 + 1/3 + ... + 1/n

# Nhập số nguyên n.
# Tính tổng dãy số.

n = int(input('Nhap so nguyen n: '))
tong = 0
for i in range(1,n+1):
    tong = tong + 1/i
print(tong)