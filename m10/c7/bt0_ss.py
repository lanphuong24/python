## Toán 10 - Kiểm tra 2 vector có song song không

# Chương trình nhận vào:
#   Vector u(a1;b1) và vector v(a2;b2)
# Trả về True nếu song song, False nếu không
# VD: u(1;2),  v(2;4)   => True
#     u(1;0),  v(0;1)   => False
#     u(2;-1), v(-4;2)  => True

pass

a1, b1 = map(int, input("Nhập vector u(a1;b1): ").split())
a2, b2 = map(int, input("Nhập vector v(a2;b2): ").split())
print(vec_song_song([a1, b1], [a2, b2]))
