## Tìm số nhỏ nhất

# Chương trình cung cấp code nhập vào danh sách các số thực
# Viết chương trình tìm số nhỏ nhất trong danh sách

print("Nhập danh sách số thực. VD: \"8 4 6 7\": ")
a = list(map(float, input().split()))

print("Danh sách nhập vào: ", a)

soNhoNhat = a[0]
for e in a:
    if e < soNhoNhat:
        soNhoNhat = e

print("Số nhỏ nhất: ", soNhoNhat)

# Trong python có hỗ trợ sẵng hàm tìm phần tử nhỏ nhất không?