## Tìm ước số

# Nhập số nguyên n
# In ra các ước số của nó từ 1 đến n

n = int(input("nhap so nguyen:"))
print("cac uoc so cua", n, end=": ")
for y in range(1, n + 1):
    if n % y == 0:
        print(y, end=", ")