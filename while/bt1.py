## Tính tổng số chẵn từ 1 đến n

# Nhập số nguyên n
# Tính tổng số chẵn từ 1 đến n và in ra kết quả

n = int(input("nhap so nguyen n: "))
i = 1
t = 0
while i <= n:
    if i % 2 == 0:
        t += i
    i += 1
print("ket qua:", t)