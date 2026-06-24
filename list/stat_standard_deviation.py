## Thống kê - Tính giá trị Độ lệch chuẩn

# Chương trình cung cấp code nhập vào dữ liệu số nguyên
# Viết chương trình tính giá trị Độ lệch chuẩn
import math

print("Nhập dữ liệu. VD: \"4 6 9 6 3 7\":")
a = list(map(int, input().split()))

print("Dữ liệu đã nhập:", a)

doLechChuan = 0
phuongSai = 0

tb = sum(a) / len(a)
total = 0
for i in a:
    total += (i - tb) ** 2
phuongSai = total / len(a)
doLechChuan = round(math.sqrt(phuongSai), 2)

print("Độ lệch chuẩn (standard deviation):", doLechChuan)