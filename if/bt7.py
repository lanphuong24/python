## Xét tuyển đại học

# Nhập điểm 3 môn thi: toán, tiếng anh, tin học
# Tính tổng điểm 3 môn
# Nếu tổng điểm lớn hơn hoặc bằng 15, sẽ xét thêm:
#   - Nếu tổng điểm lớn hơn hoặc bằng 24, thông báo "Bạn đã đậu trường PTIT"
#   - Nếu tổng điểm lớn hơn hoặc bằng 21, thông báo "Bạn đã đậu trường HUB"
#   - Nếu tổng điểm lớn hơn hoặc bằng 18, thông báo "Bạn đã đậu trường FTU"
#   - Nếu tổng điểm dưới 18, thông báo "Bạn đã đậu TDU"
# Nếu tổng điểm dưới 15, thông báo "Rớt tốt nghiệp"

to = float(input("nhap diem toan: "))
ta = float(input("nhap diem tieng anh: "))
th = float(input("nhap diem tin hoc: "))
tt = to + ta + th
if tt >= 15:
    if tt >= 24:
        print("ban da dau truong PTIT")
    elif tt >= 21:
        print("ban da dau truong HUB")
    elif tt >= 18:
        print("ban dau truong FTU")
    else:
        print("ban da dau TDU")
else:
    print("rot tot nghiep")