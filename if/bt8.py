## Kiểm tra tam giác cân

# Nhập 3 cạnh của tam giác
# Kiểm tra tam giác đã cho có phải tam giác cân hay không
# Gợi ý: chỉ cần 2 cạnh bất kỳ bằng nhau thì tam giác đã cho là tam giác cân

canh1 = float(input('Nhap canh 1: '))
canh2 = float(input('Nhap canh 2: '))
canh3 = float(input('Nhap canh 3: '))
if canh1 == canh2 or canh2 == canh3 or canh3 == canh1:
    print('Day la tam giac can.')
else:
    print('Day khong phai la tam giac can')
