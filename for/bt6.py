## In bảnh cửu chương

# Nhập số bảng cửu chương
# VD: Cửu chương 7
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

n = int(input("nhap so bang cuu chuong: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)