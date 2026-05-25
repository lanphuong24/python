## Kiểm tra lên lớp

# Nhập điểm trung bình (ĐTB) và hạnh kiểm (tốt, khá, trung bình, yếu)
# Nếu ĐTB lớn hơn hoặc bằng 5, kiểm tra thêm hạng kiểm:
#   - Hạng kiểm tốt hoặc khá, được lên lớp
#   - Hạng kiểm trung bình hoặc yếu, sẽ xem xét thêm
# Nếu ĐTB dưới 5, ở lại lớp

dtb = float(input("nhap diem trung binh: "))
if dtb >= 5:
    hk = input("hanh kiem (tot, kha, trung binh, yeu): ")
    if hk == "tot" or hk == "kha":
        print("len lop")
    else:
        print("xem xet them")
else:
    print("o lai lop")
