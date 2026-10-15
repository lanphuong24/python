## In số lẻ

# Nhập số nguyên n
# In các số lẻ từ 1 đến n.

n = int(input('Nhap n: '))
for i in range(n+1):
    if i%2 != 0:
        print(i)
