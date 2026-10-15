## Tìm ước số

# Nhập số nguyên n
# In ra các ước số của nó từ 1 đến n

n = int(input('Nhap so nguyen n: '))
for i in range(1,n+1):
    if n%i ==0:
        print(i)