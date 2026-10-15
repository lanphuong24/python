## Tính tổng dãy số 1 + 2 + 3 + ... + n

# Nhập số nguyên n
# Tính và in ra tổng dãy số từ 1 đến n

n = int(input('Nhap so nguyen n: '))
s = 0
for i in range(1,n+1):
    s = s+i
print(s)