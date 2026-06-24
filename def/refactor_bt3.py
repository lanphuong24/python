## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới kiểm tra và in thông tin cho nhiều xâu
# Hãy viết hàm analyze và thay thế các đoạn lặp lại bằng lời gọi hàm

s1 = "Tin học"
print(f"Xâu: '{s1}'")
print(f"  Độ dài: {len(s1)}")
print(f"  Chữ hoa: {s1.upper()}")
print(f"  Đảo ngược: {s1[::-1]}")

s2 = "Python"
print(f"Xâu: '{s2}'")
print(f"  Độ dài: {len(s2)}")
print(f"  Chữ hoa: {s2.upper()}")
print(f"  Đảo ngược: {s2[::-1]}")

s3 = "Lập trình"
print(f"Xâu: '{s3}'")
print(f"  Độ dài: {len(s3)}")
print(f"  Chữ hoa: {s3.upper()}")
print(f"  Đảo ngược: {s3[::-1]}")
