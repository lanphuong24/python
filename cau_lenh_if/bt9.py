## Kiểm tra số lớn nhất

# Nhập 3 số
# In ra tổng 3 số
# In ra số lớn nhất

so1 = float(input("nhap so 1: "))
so2 = float(input("nhap so 2: "))
so3 = float(input("nhap so 3: "))
tong = so1 + so2 + so3
print("tong 3 so:", tong)
max = so1
if so2 > max:
    max = so2
if so3 > max:
    max = so3
print("so lon nhat:", max)
min = so1
if so2 < min:
    min = so2
if so3 < min:
    min = so3
print("so nho nhat:", min)