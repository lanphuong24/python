## In hình vuông dấu *

# Nhập số nguyên n.
# In hình vuông gồm n dòng và n cột dấu *
# VD: n = 4
# * * * *
# * * * *
# * * * *
# * * * *

n = int(input('Nhap so nguyen n: '))
for i in range(1,n+1):
    print('*'*n)