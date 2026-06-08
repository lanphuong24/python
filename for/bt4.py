## Kiểm tra số hoàn hảo

# Nhập số nguyên n
# Kiểm tra n có phải là số hoàn hảo hay không. 
# n được gọi là số hoàn hảo nếu tổng các ước số của nó (không bao gồm n) bằng chính nó.

n = int(input("nhap so nguyen: "))
t = 0
for i in range(1, n):
    if n % i == 0:
        t += i
if t == n:
    print(n, "la so hoan hao")
else:
    print(n, "khong phai la so hoan hao")
