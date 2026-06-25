## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới xử lý điểm cho nhiều học sinh
# Hãy viết hàm xep_loai và thay thế các đoạn lặp lại bằng lời gọi hàm

def xep_loai(ten, diem):
    if diem >= 8:
        loai = "Giỏi"
    elif diem >= 6.5:
        loai = "Khá"
    elif diem >= 5:
        loai = "Trung bình"
    else:
        loai = "Yếu"
    print(f"{ten}: {diem} - {loai}")

xep_loai("An", 8.5)
xep_loai("Binh", 6.0)
xep_loai("Chau", 4.0)