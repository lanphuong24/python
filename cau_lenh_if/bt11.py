## Tính tiền điện

# Nhập chỉ số điện dùng trong tháng (đơn vị kw)
# Tính số tiền tương ứng với chỉ số điện đã dùng. Cách tính như sau:
#   - Mỗi kw trong 100 kw đầu tiên có giá 2,000 VNĐ / kw
#   - Từ kw thú 101 đến 200, có giá 2,500 VNĐ / kw
#   - Từ kw thứ 200 trở lên có giá 3,000 VNĐ / kw

ld = int(input("so dien da dung (don vi kw): "))
if ld > 200:
    d3 = ld - 200
    t3 = d3 * 3000
    tt = t3 + 100 * 2000 + 100 * 2500
elif ld > 100:
    d2 = ld - 100
    t2 = d2 * 2500
    tt = t2 + 100 * 2000
else:
    tt = ld * 2000
print("tien dien:", tt)