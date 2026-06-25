## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới tính diện tích hình chữ nhật nhiều lần
# Hãy viết hàm area và thay thế các đoạn tính lặp lại bằng lời gọi hàm

def s(d, r):
    return d * r

print(f"Diện tích HCN 1: {s(5, 3)}")
print(f"Diện tích HCN 2: {s(8, 4)}")
print(f"Diện tích HCN 3: {s(10, 6)}")
