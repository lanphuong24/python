## Kiểm tra vào hồ bơi

# Nhập khảo sát: Biết bơi không? Có áo phao không?
# Nếu biết bơi, thông báo "Cho xuống hồ"
# Nếu không biết bơi, kiểm tra áo phao:
#   - Có áo phao, thông báo "Được xuống hồ"
#   - Không có áo phao, thông báo "Nguy hiểm"

bbk = input('Biet boi khong? ')
capk = input('Co ao phao khong? ')
if bbk == 'Co':
    print('Cho xuong ho')
else:
    if capk == 'Co':
        print('Duoc xuong ho')
    else:
        print('Nguy hiem')