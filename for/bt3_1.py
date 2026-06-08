## Kiểm tra số nguyên tố

# Nhập số nguyên n
# Kiểm tra n có phải là số nguyên tố hay không.

n = int(input("nhap so nguyen:"))
uocso = 0
for y in range(1, n + 1):
    if n % y == 0:
        uocso = uocso + 1

if uocso == 2:
    print(n, "la so nguyen to")
else:
    print("kphai so nguyen to")
