## In hình vuông dấu *

# Nhập số nguyên n.
# In hình vuông gồm n dòng và n cột dấu *
# VD: n = 4
# * * * *
# * * * *
# * * * *
# * * * *

n = int(input("nhap so nguyen n: "))

for d in range(n):
    for c in range(n):
        print("*", end=" ")
    print()