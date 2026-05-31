## Đếm ước số

# Nhập số nguyên n
# Tính và in ra tổng ước số của n từ 1 đến chính nó

n = int(input("nhap so nguyen n: "))
i = 1
t = 0
while i <= n:
    if n % i == 0:
        t += i
    i += 1
print("ket qua:", t)