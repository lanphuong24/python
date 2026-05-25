## Kiểm tra tam giác cân

# Nhập 3 cạnh của tam giác
# Kiểm tra tam giác đã cho có phải tam giác cân hay không
# Gợi ý: chỉ cần 2 cạnh bất kỳ bằng nhau thì tam giác đã cho là tam giác cân

c1 = int(input("cạnh 1: "))
c2 = int(input("cạnh 2: "))
c3 = int(input("cạnh 3: "))
if c1 > 0 and c2 > 0 and c3 > 0:
    if c1 == c2 or c2 == c3 or c3 == c1:
        print("tam giac can")
    else:
        print("khong phai")
else:
    print("du lieu k hop le")
