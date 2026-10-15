## Kiểm tra số hoàn hảo

# Nhập số nguyên n
# Kiểm tra n có phải là số hoàn hảo hay không. 
# n được gọi là số hoàn hảo nếu tổng các ước số của nó (không bao gồm n) bằng chính nó.

n = int(input('Nhap so nguyen n: '))
tong = 0
for i in range(1,n):
    if n%i ==0:
        tong = tong + i
if tong == n:
    print('n la so hoan hao')
else:
    print('n khong phai la so hoan hao')