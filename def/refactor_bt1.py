## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới in bảng cửu chương cho nhiều số
# Hãy viết hàm print_table và thay thế các đoạn lặp lại bằng lời gọi hàm

def kq(n):
    print(f"Bảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

kq(2)
kq(3)
kq(5)
