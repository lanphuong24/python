## Truy xuất mảng hai chiều bằng vòng lặp

# Mỗi hàng gồm: tên học sinh, điểm Toán, điểm Lý, điểm Hóa
hocsinh = [
    ["An", 8, 7, 9],
    ["Bình", 6, 8, 7],
    ["Chi", 9, 8, 10],
    ["Dũng", 7, 6, 8]
]

# Sửa code bên dưới để in thông tin của mỗi học sinh trên một dòng
# Code phải đảm bảo vẫn đúng khi thêm hoặc xóa học sinh
# Kết quả mong đợi:
# ["An", 8, 7, 9]
# ["Bình", 6, 8, 7]
# ...
for hoc_sinh in hocsinh:
    pass

# Sửa code bên dưới để in tên của tất cả học sinh,
# mỗi tên trên một dòng
for hoc_sinh in hocsinh:
    pass

# Sửa code bên dưới để in từng giá trị trong mảng
# Mỗi học sinh được in trên một dòng, các giá trị cách nhau bởi dấu cách
# Kết quả mong đợi:
# An 8 7 9
# Bình 6 8 7
# ...
for hang in hocsinh:
    for gia_tri in hang:
        pass

# Sửa code bên dưới để tính và in ra điểm trung bình môn Hóa
# Code phải đảm bảo vẫn đúng khi thay đổi điểm hoặc danh sách học sinh
diem_trung_binh_hoa = 0
pass
print("Điểm trung bình môn Hóa:", diem_trung_binh_hoa)

# Sửa code bên dưới để tìm và in ra điểm Toán cao nhất
# Không sử dụng hàm max()
# Code phải đảm bảo vẫn đúng khi thay đổi điểm hoặc danh sách học sinh
diem_toan_cao_nhat = 0
pass
print("Điểm Toán cao nhất:", diem_toan_cao_nhat)
