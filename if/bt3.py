## Xếp loại dựa trên điểm trung bình

# Nhập điểm trung bình cho học sinh
# Xếp loại điểm cho học sinh:
# Từ 9 trở lên => Xuất sắc
# Từ 8 đến 9 => Giỏi
# Từ 7 đến 8 => Khá
# Từ 5 trở lên => Trung bình
# Các trường hợp còn lại => Yếu

diemtb = int(input('Nhap diem trung binh: '))
if diemtb >= 9:
    print('Xuat sac')
elif diemtb >= 8:
    print('Gioi')
elif diemtb >= 7:
    print('Kha')
elif diemtb >= 5:
    print('Trung binh')
else:
    print('Yeu')