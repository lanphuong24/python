## Tách xâu (split)

s = "An Bình Châu Dũng"

# Tách xâu s thành danh sách các tên
# In ra tên đầu tiên và tên cuối cùng
# In ra số lượng tên trong xâu
# Code phải đảm bảo vẫn đúng khi sửa đổi xâu s

names = s.split(" ")

firstName = names[0]
lastName = names[-1]
count = len(names)

print("Danh sách:", names)
print("Tên đầu:", firstName)
print("Tên cuối:", lastName)
print("Số lượng:", count)
