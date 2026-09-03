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
    print(hoc_sinh)
    pass

# Sửa code bên dưới để in tên của tất cả học sinh,
# mỗi tên trên một dòng
for hoc_sinh in hocsinh:
    print(hoc_sinh[0])
    pass

# Sửa code bên dưới để in từng giá trị trong mảng
# Mỗi học sinh được in trên một dòng, các giá trị cách nhau bởi dấu cách
# Kết quả mong đợi:
# An 8 7 9
# Bình 6 8 7
# ...
for hs in hocsinh:
    print(hs[0], hs[1], hs[2], hs[3])

# Sửa code bên dưới để tính và in ra điểm trung bình môn Hóa
# Code phải đảm bảo vẫn đúng khi thay đổi điểm hoặc danh sách học sinh

a = hocsinh[0][3]
b = hocsinh[1][3]
c = hocsinh[2][3]
d = hocsinh[3][3]
e = diem_trung_binh_hoa = (a+b+c+d)/4
print("Điểm trung bình môn Hóa:", diem_trung_binh_hoa)

# Sửa code bên dưới để tìm và in ra điểm Toán cao nhất
# Không sử dụng hàm max()
# Code phải đảm bảo vẫn đúng khi thay đổi điểm hoặc danh sách học sinh
diem_toan_cao_nhat = hocsinh[0][1]
for hs in hocsinh:
    if hs[1] > diem_toan_cao_nhat:
        diem_toan_cao_nhat = hs[1]
    
print("Điểm Toán cao nhất:", diem_toan_cao_nhat)
