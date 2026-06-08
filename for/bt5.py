## Tìm số 3 chữ số

# Viết chương trình tìm tất cả số có 3 chữ số sao cho tổng tất cả các chữ số bằng tích của chúng

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if a + b + c == a * b * c:
                print(a, b, c)
                pass