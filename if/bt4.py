## Mua vé xem phim

# Nhập tuổi và số tiền
# Nếu tuổi lớn hơn hoặc bằng 18, kiểm tra thêm:
#   - Nếu tiền lớn hơn hoặc bằng $100, thông báo "Được vào rạp"
#   - Nếu tiền ít hơn $100, thông báo "Không đủ tiền"
# Nếu tuổi nhỏ hơn 18, thông báo "Không đủ tuổi"

tuoi = int(input('Nhap tuoi: '))
tien = int(input('Nhap tien: '))
if tuoi >= 18:
    if tien >= 100:
        print('Duoc vao rap')
    else:
        print('Khong du tien')
else:
    print('Khong du tuoi')
    