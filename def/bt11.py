## Định nghĩa hàm - Hàm gọi hàm con

# Hàm trung_binh đã được viết sẵn, dùng hàm con tong để tính
# Viết hàm con tong(a) trả về tổng các phần tử trong danh sách a
# Không được dùng hàm sum() có sẵn
# vd: tong([1, 2, 3, 4]) => 10

def tong(a):
    pass


def trung_binh(a):
    return tong(a) / len(a)


print(trung_binh([1, 2, 3, 4]))    # 2.5
print(trung_binh([10, 20, 30]))    # 20.0
print(trung_binh([5]))             # 5.0
