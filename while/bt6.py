## Trò chơi đoán số

# Chương trình phát sinh số ngẫu nhiên từ 1 đến 10
# Người chơi tham gia đoán đố đó, được đoán 3 lần.
# Nếu người chơi đoán trúng, thông báo chiến thắng và dừng trò chơi.
# Nếu sau 3 lần đoán thất bại, thông báo thua cuộc, hiển thị số bí mật, và dừng trò chơi.

import random

soBiMat = random.randint(1, 10)

i = 1
thang = False
while not thang and i <= 3:
    n = int(input("nhap so tu 1-10: "))
    if n == soBiMat:
        print("chien thang")
        thang = True
        break
    else:
        print("doan sai")
    i += 1

if not thang:
    print("ban doan sai 3 lan. dap an la:", soBiMat)