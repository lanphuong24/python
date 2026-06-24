## Thống kê - Tính giá trị Trung vị

# Chương trình cung cấp code nhập vào dữ liệu số nguyên
# Viết chương trình tính giá trị Trung vị (Me)

print("Nhập dữ liệu. VD: \"4 6 9 6 3 7\":")
a = list(map(int, input().split()))
a.sort()

print("Dữ liệu đã nhập:", a)

median = 0
cdai = len(a)
if cdai % 2 == 0:
    median = (a[cdai//2-1] + a[(cdai//2-1)+1]) / 2
else:
    median = a[cdai//2] 

print("Trung vị (Me):", median)