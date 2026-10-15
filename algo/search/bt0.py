## Đọc file - Nhân đôi một số

# File bt0.inp gồm 10 số nguyên, mỗi số trên một dòng.
# Đọc dữ liệu vào list a.
# Nhân đôi từng số và thêm vào list ket_qua.
# Ghi kết quả vào bt0.out, mỗi kết quả trên một dòng tương ứng.
# Chạy chương trình trong thư mục algo/search.

inp = open("algo/search/bt0.inp", "r")
a = []
for dong in inp:
    a.append(int(dong))
inp.close()

out = open("algo/search/bt0.out", "w")
for e in a:
    print(e * 2, file=out)
out.close()
