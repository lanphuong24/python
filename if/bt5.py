## Kiểm tra vào hồ bơi

# Nhập khảo sát: Biết bơi không? Có áo phao không?
# Nếu biết bơi, thông báo "Cho xuống hồ"
# Nếu không biết bơi, kiểm tra áo phao:
#   - Có áo phao, thông báo "Được xuống hồ"
#   - Không có áo phao, thông báo "Nguy hiểm"

boi = input("biet boi khong? tra loi bang co hoac ko: ")
if boi == "co":
    print("cho xuong ho")
else:
    ao = input("co ao phao khong? tra loi bang co hoac ko: ")
    if ao == "co":
        print("duoc xuong ho")
    else:
        print("nguy hiem")
