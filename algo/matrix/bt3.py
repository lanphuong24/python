## Nhập mảng hai chiều từ bàn phím

# Viết chương trình thực hiện các yêu cầu sau:
# 1. Nhập số lượng sinh viên.
# 2. Nhập thông tin của từng sinh viên trên một dòng.
#    Mỗi dòng gồm: tên, điểm Toán, điểm Lý, điểm Hóa.
#    Ví dụ: An 8 7 9
# 3. Lưu thông tin vào mảng hai chiều sinhvien.
# 4. In lại danh sách sinh viên vừa nhập, mỗi sinh viên trên một dòng.
dshs = []
n = int(input("Số lượng sinh viên:"))
for i in range(1, n+1):
    a = list(map(str, input(f"Thông tin của sinh viên {i}:").split()))
    a[1] = float(a[1])
    a[2] = float(a[2])
    a[3] = float(a[3])
    dshs.append(a)
for hs in dshs:
    print(hs)
