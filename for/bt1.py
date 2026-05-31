## In số lẻ

# Nhập số nguyên n
# In các số lẻ từ 1 đến n.

n = int(input("nhap so nguyen: "))
for y in range(n + 1):
    if y % 2 != 0:
        print("so le:", y)
