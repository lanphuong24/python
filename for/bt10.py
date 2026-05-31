## In tam giác vuông dấu *

# Nhập số nguyên n.
# In tam giác vuông bằng dấu *
# VD: n = 4
# *
# * *
# * * *
# * * * *

n = int(input("nhap so nguyen n: "))

for d in range(1, n + 1):
    for c in range(d):
        print("*", end=" ")
    print()