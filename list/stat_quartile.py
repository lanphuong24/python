## Thống kê - Tính giá trị Tứ trung vị Q1, Q2, Q3, IQR

# Chương trình cung cấp code nhập vào dữ liệu số nguyên
# Viết chương trình tính giá trị Q1, Q2, Q3, IQR

print("Nhập dữ liệu. VD: \"4 6 9 6 3 7\":")
a = list(map(int, input().split()))
a.sort()

print("Dữ liệu đã nhập:", a)

q1 = 0
q2 = 0
q3 = 0
iqr = 0

cdai = len(a)
if cdai % 2 == 0:
    q2 = (a[cdai//2-1] + a[(cdai//2-1)+1]) / 2
else:
    q2 = a[cdai//2] 

list1 = []
list2 = []
if cdai % 2 == 0:
    list1 = a[:cdai//2]
    list2 = a[cdai//2:]
else:
    list1 = a[:cdai//2]
    list2 = a[cdai//2+1:]

cdai = len(list1)
if cdai % 2 == 0:
    q1 = (list1[cdai//2-1] + list1[(cdai//2-1)+1]) / 2
else:
    q1 = list1[cdai//2] 

cdai = len(list2)
if cdai % 2 == 0:
    q3 = (list2[cdai//2-1] + list2[(cdai//2-1)+1]) / 2
else:
    q3 = list2[cdai//2] 

iqr = q3 - q1


print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("IQR:", iqr)