## Thống kê - Tính giá trị trung bình

# Chương trình cung cấp code nhập vào danh sách điểm của học sinh
# Viết chương trình tính giá trị trung bình (average)

print("Nhập danh sách điểm. VD: \"10 4.5 3 7\": ")
a = list(map(float, input().split()))

print("Danh sách điểm nhập vào:", a)

total = 0
for e in a:
    total += e
average = total / len(a)


print("Điểm trung bình (average):", average)