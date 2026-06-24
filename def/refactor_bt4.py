## Refactor - Đưa code lặp lại vào hàm

# Code bên dưới tính tứ phân vị cho nhiều bộ dữ liệu
# Lưu ý: cách tính Q1, Q2, Q3 dùng trung vị của từng nửa danh sách
# Hãy viết hàm quartile(a) trả về list [q1, q2, q3, iqr]
# và thay thế các đoạn lặp lại bằng lời gọi hàm

a1 = [4, 6, 9, 6, 3, 7]
a1.sort()
n1 = len(a1)
if n1 % 2 == 0:
    q2_1 = (a1[n1//2 - 1] + a1[n1//2]) / 2
    lower1 = a1[:n1//2]
    upper1 = a1[n1//2:]
else:
    q2_1 = a1[n1//2]
    lower1 = a1[:n1//2]
    upper1 = a1[n1//2+1:]
q1_1 = (lower1[len(lower1)//2 - 1] + lower1[len(lower1)//2]) / 2 if len(lower1) % 2 == 0 else lower1[len(lower1)//2]
q3_1 = (upper1[len(upper1)//2 - 1] + upper1[len(upper1)//2]) / 2 if len(upper1) % 2 == 0 else upper1[len(upper1)//2]
iqr1 = q3_1 - q1_1
print(f"Dữ liệu: {a1} => Q1={q1_1}, Q2={q2_1}, Q3={q3_1}, IQR={iqr1}")

a2 = [2, 4, 4, 5, 6, 7, 8]
a2.sort()
n2 = len(a2)
if n2 % 2 == 0:
    q2_2 = (a2[n2//2 - 1] + a2[n2//2]) / 2
    lower2 = a2[:n2//2]
    upper2 = a2[n2//2:]
else:
    q2_2 = a2[n2//2]
    lower2 = a2[:n2//2]
    upper2 = a2[n2//2+1:]
q1_2 = (lower2[len(lower2)//2 - 1] + lower2[len(lower2)//2]) / 2 if len(lower2) % 2 == 0 else lower2[len(lower2)//2]
q3_2 = (upper2[len(upper2)//2 - 1] + upper2[len(upper2)//2]) / 2 if len(upper2) % 2 == 0 else upper2[len(upper2)//2]
iqr2 = q3_2 - q1_2
print(f"Dữ liệu: {a2} => Q1={q1_2}, Q2={q2_2}, Q3={q3_2}, IQR={iqr2}")

a3 = [1, 3, 5, 7, 9, 11, 13, 15]
a3.sort()
n3 = len(a3)
if n3 % 2 == 0:
    q2_3 = (a3[n3//2 - 1] + a3[n3//2]) / 2
    lower3 = a3[:n3//2]
    upper3 = a3[n3//2:]
else:
    q2_3 = a3[n3//2]
    lower3 = a3[:n3//2]
    upper3 = a3[n3//2+1:]
q1_3 = (lower3[len(lower3)//2 - 1] + lower3[len(lower3)//2]) / 2 if len(lower3) % 2 == 0 else lower3[len(lower3)//2]
q3_3 = (upper3[len(upper3)//2 - 1] + upper3[len(upper3)//2]) / 2 if len(upper3) % 2 == 0 else upper3[len(upper3)//2]
iqr3 = q3_3 - q1_3
print(f"Dữ liệu: {a3} => Q1={q1_3}, Q2={q2_3}, Q3={q3_3}, IQR={iqr3}")
