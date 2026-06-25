## Định nghĩa hàm

# Viết hàm sum_list nhận vào một danh sách số, trả về tổng
# Không được dùng hàm sum() có sẵn
# vd: sum_list([1, 2, 3, 4]) => 10

def sum_list(a):
    tong = 0
    for i in a:
        tong += i
    return tong

print(sum_list([1, 2, 3, 4]))     # 10
print(sum_list([10, -5, 3]))      # 8
print(sum_list([]))               # 0
