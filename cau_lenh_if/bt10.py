## Đổi thời gian

# Nhập tổng số giây
# Đổi và in ra số giờ số phút số giây còn lại trên tổng số giây đó
# VD: 70 giây => 0 giờ, 1 phút, 10 giây

tsg = int(input("tong so giay: "))
h = tsg // 3600
m = (tsg % 3600) // 60
s = (tsg % 3600) % 60
print("doi tg:", h, m, s)