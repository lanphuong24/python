## Kiểm tra số nguyên tố

# Nhập số nguyên n
# Kiểm tra n có phải là số nguyên tố hay không.

n = int(input('Nhap so nguyen n: '))
uocso = 0
for i in range(1,n+1):
    if n%i ==0:
        uocso = uocso+1
if uocso <=2:
    print('n la so nguyen to')
else:
    print('n khong phai la so nguyen to')
