## Định nghĩa hàm - Hàm gọi hàm con

# Hàm xep_loai_hs đã được viết sẵn, dùng hàm con tinh_xep_loai để xếp loại
# Viết hàm con tinh_xep_loai(diem) trả về xâu xếp loại tương ứng
# vd: tinh_xep_loai(8.5) => "Giỏi"
#     tinh_xep_loai(6.5) => "Khá"
#     tinh_xep_loai(5.0) => "Trung bình"
#     tinh_xep_loai(4.0) => "Yếu"

def tinh_xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu" 


def xep_loai_hs(ten, diem):
    loai = tinh_xep_loai(diem)
    print(f"{ten}: {diem} - {loai}")


xep_loai_hs("An", 8.5)     # An: 8.5 - Giỏi
xep_loai_hs("Bình", 6.5)   # Bình: 6.5 - Khá
xep_loai_hs("Châu", 5.0)   # Châu: 5.0 - Trung bình
xep_loai_hs("Dũng", 4.0)   # Dũng: 4.0 - Yếu
