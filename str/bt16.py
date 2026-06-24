## Mã ASCII / Unicode của ký tự

# Nhập vào một xâu, in ra mã Unicode của từng ký tự
# vd: "ABC" =>
# A : 65
# B : 66
# C : 67
# Gợi ý: dùng ord() để lấy mã Unicode của ký tự

print("Nhập một xâu:")
s = input()

for c in s:
    code = ord(c)
    print(f"{c} : {code}\t{bin(code)}\t{hex(code)}")
