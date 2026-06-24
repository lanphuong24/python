## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới xử lý điểm cho nhiều học sinh
# Hãy viết hàm xep_loai và thay thế các đoạn lặp lại bằng lời gọi hàm

ten_1 = "An"
diem_1 = 8.5
if diem_1 >= 8:
    loai_1 = "Giỏi"
elif diem_1 >= 6.5:
    loai_1 = "Khá"
elif diem_1 >= 5:
    loai_1 = "Trung bình"
else:
    loai_1 = "Yếu"
print(f"{ten_1}: {diem_1} - {loai_1}")

ten_2 = "Bình"
diem_2 = 6.0
if diem_2 >= 8:
    loai_2 = "Giỏi"
elif diem_2 >= 6.5:
    loai_2 = "Khá"
elif diem_2 >= 5:
    loai_2 = "Trung bình"
else:
    loai_2 = "Yếu"
print(f"{ten_2}: {diem_2} - {loai_2}")

ten_3 = "Châu"
diem_3 = 4.0
if diem_3 >= 8:
    loai_3 = "Giỏi"
elif diem_3 >= 6.5:
    loai_3 = "Khá"
elif diem_3 >= 5:
    loai_3 = "Trung bình"
else:
    loai_3 = "Yếu"
print(f"{ten_3}: {diem_3} - {loai_3}")
