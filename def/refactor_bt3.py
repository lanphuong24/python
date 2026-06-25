## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới kiểm tra và in thông tin cho nhiều xâu
# Hãy viết hàm analyze và thay thế các đoạn lặp lại bằng lời gọi hàm

def s(n):
    print(f"Xâu: '{n}'")
    print(f"  Độ dài: {len(n)}")
    print(f"  Chữ hoa: {n.upper()}")
    print(f"  Đảo ngược: {n[::-1]}")

s("Tin học")
s("Python")
s("Lập trình")

