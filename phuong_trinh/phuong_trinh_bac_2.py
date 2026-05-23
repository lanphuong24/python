import math

print("giai phuong trinh bac 2 ax^2 + bx + c = 0")
a = float(input("nhap a: "))
b = float(input("nhap b: "))
c = float(input("nhap c: "))
delta = b * b - 4 * a * c
if delta < 0:
    print("phuong trinh vo nghiem")
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (b + math.sqrt(delta)) / 2 * a
    print("phuong trinh co hai nghiem phan biet")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    x = -b / 2 * a
    print("phuong trinh co nghiem kep")
    print("x =", x)