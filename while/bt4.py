## Đếm số trong dãy

# Đếm trong dãy 100 số tự nhiên đầu tiên có bao nhiêu số thoả mãn
# điều kiện: hoặc chia hết cho 5 hoặc chia cho 3 dư 1

n = 100
i = 1
while i <= n:
    if i % 5 == 0 or i % 3 == 1:
        print(i)
    i += 1
    