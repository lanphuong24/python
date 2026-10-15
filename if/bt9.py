## Kiểm tra số lớn nhất

# Nhập 3 số
# In ra tổng 3 số
# In ra số lớn nhất

a = int(input('Nhap so thu 1: '))
b = int(input('Nhap so thu 2: '))
c = int(input('Nhap so thu 3: '))
tong = a + b + c

sln = a
if b > sln:
    sln = b
if c > sln:
    sln = c
print('so lon nhat la', sln)