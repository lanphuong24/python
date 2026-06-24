## Thống kê - Tính giá trị mốt

# Chương trình cung cấp code nhập vào dữ liệu số nguyên
# Viết chương trình tính giá trị mốt (mode)

print("Nhập dữ liệu. VD: \"4 6 9 6 3 7\":")
a = list(map(int, input().split()))

print("Dữ liệu đã nhập:", a)

mode = [a[0]]
soLonNhat = 0
for i in a:
    times = a.count(i)
    if soLonNhat < times:
        soLonNhat = times
        mode = [i]
    elif soLonNhat == times:
        if i not in mode:
            mode.append(i)
if len(mode) == 1 or len(mode) == 2:
    print("Mốt (mode):", mode)
else:
    print("Khong co mot")