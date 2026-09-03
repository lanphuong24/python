## Truy xuất phần tử trong mảng hai chiều

# Mỗi hàng gồm: tên học sinh, điểm Toán, điểm Lý, điểm Hóa
hocsinh = [
    ["An", 8, 7, 9],
    ["Bình", 6, 8, 7],
    ["Chi", 9, 8, 10],
    ["Dũng", 7, 6, 8]
]

# Sửa code bên dưới để in ra toàn bộ thông tin của học sinh An
thong_tin_an = hocsinh[0]
print("Thông tin của An:", thong_tin_an)

# Sửa code bên dưới để in ra tên của học sinh thứ hai
ten_hoc_sinh_thu_hai = hocsinh[1][0]
print("Tên học sinh thứ hai:", ten_hoc_sinh_thu_hai)

# Sửa code bên dưới để in ra điểm Lý của An
diem_ly_cua_an = hocsinh[0][2]
print("Điểm Lý của An:", diem_ly_cua_an)

# Sửa code bên dưới để in ra điểm Hóa của Bình
diem_hoa_cua_binh = hocsinh[1][3]
print("Điểm Hóa của Bình:", diem_hoa_cua_binh)

# Sửa code bên dưới để in ra số học sinh trong danh sách
# Code phải đảm bảo vẫn đúng khi thêm hoặc xóa học sinh
so_hoc_sinh = len(hocsinh)
print("Số học sinh:", so_hoc_sinh)
