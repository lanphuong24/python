## Mua vé xem phim

# Nhập tuổi và số tiền
# Nếu tuổi lớn hơn hoặc bằng 18, kiểm tra thêm:
#   - Nếu tiền lớn hơn hoặc bằng $100, thông báo "Được vào rạp"
#   - Nếu tiền ít hơn $100, thông báo "Không đủ tiền"
# Nếu tuổi nhỏ hơn 18, thông báo "Không đủ tuổi"

tuoi = int(input("nhap tuoi: "))
#tien = int(input("nhap so tien: "))
if tuoi >= 18:
    tien = int(input("nhap so tien: "))
    if tien >= 100:
      print("duoc vao rap")
    else:
       print("khong du tien")
else:
   print("khong du tuoi")
   
