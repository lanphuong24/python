## Toán 10 - Lập phương trình chính tắc parabol đi qua điểm M
# Parabol dạng chính tắc: y^2 = 2px  (p > 0)

# Chương trình nhận vào:
#   Tọa độ điểm M(x0;y0) thuộc parabol (x0 > 0)
# Trả về:
#   Chuỗi phương trình dạng y^2 = 2px
# VD: M(2;4)   => y^2 = 8x
#     M(8;4)   => y^2 = 2x
# Gợi ý:
#   M thuộc parabol => y0^2 = 2p*x0
#   => p = y0^2 / (2*x0)

def pt_parabol(M):
    p = M[1]**2 / (2*M[0])
    return f" y^2 = {2*p}x "


x0, y0 = map(float, input("Nhập tọa độ M (x0;y0): ").split())
print(pt_parabol([x0, y0]))
