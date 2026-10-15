## Xét tuyển đại học

# Nhập điểm 3 môn thi: toán, tiếng anh, tin học
# Tính tổng điểm 3 môn
# Nếu tổng điểm lớn hơn hoặc bằng 15, sẽ xét thêm:
#   - Nếu tổng điểm lớn hơn hoặc bằng 24, thông báo "Bạn đã đậu trường PTIT"
#   - Nếu tổng điểm lớn hơn hoặc bằng 21, thông báo "Bạn đã đậu trường HUB"
#   - Nếu tổng điểm lớn hơn hoặc bằng 18, thông báo "Bạn đã đậu trường FTU"
#   - Nếu tổng điểm dưới 18, thông báo "Bạn đã đậu TDU"
# Nếu tổng điểm dưới 15, thông báo "Rớt tốt nghiệp"

diemT = int(input('Nhap diem toan: '))
diemTA = int(input('Nhap diem tieng anh: '))
diemTH = int(input('Nhap diem tin hoc: '))
tongdiem = diemT + diemTA + diemTH
if tongdiem >= 15:
    if tongdiem >= 24:
        print('Ban da dau truong PTIT')
    elif tongdiem >= 21:
        print('Ban da dau truong HUB')
    elif tongdiem >=18:
        print('Ban da dau truong FTU')
    else:
        print('Ban da dau TDU')
else:
    print('Rot tot nghiep')