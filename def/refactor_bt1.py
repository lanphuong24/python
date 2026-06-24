## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới in bảng cửu chương cho nhiều số
# Hãy viết hàm print_table và thay thế các đoạn lặp lại bằng lời gọi hàm

print("Bảng cửu chương 2:")
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")

print("Bảng cửu chương 3:")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

print("Bảng cửu chương 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
