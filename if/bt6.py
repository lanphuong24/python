## Kiểm tra lên lớp

# Nhập điểm trung bình (ĐTB) và hạnh kiểm (tốt, khá, trung bình, yếu)
# Nếu ĐTB lớn hơn hoặc bằng 5, kiểm tra thêm hạng kiểm:
#   - Hạng kiểm tốt hoặc khá, được lên lớp
#   - Hạng kiểm trung bình hoặc yếu, sẽ xem xét thêm
# Nếu ĐTB dưới 5, ở lại lớp

dtb = float(input('Nhap diem trung binh: '))
hanhkiem = input('Nhap hanh kiem: ')
if dtb >= 5:
    if hanhkiem == 'tot' or hanhkiem == 'kha':
        print('Duoc len lop')
    else:
        print('Dang xem xet')
else:
    print('O lai lop')
