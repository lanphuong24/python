## Xếp loại dựa trên điểm trung bình

# Nhập điểm trung bình cho học sinh
# Xếp loại điểm cho học sinh:
# Từ 9 trở lên => Xuất sắc
# Từ 8 đến 9 => Giỏi
# Từ 7 đến 8 => Khá
# Từ 5 trở lên => Trung bình
# Các trường hợp còn lại => Yếu

d = float(input("nhap diem trung binh cho hoc sinh: "))
if d >= 9:
    print("xuat sac")
elif d >= 8:
    print("gioi")
elif d >= 7:
    print("kha")
elif d >= 5:
    print("trung binh")
else:
    print("yeu")