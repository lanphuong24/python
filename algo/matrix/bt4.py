## Đọc dữ liệu ma trận từ tập tin và xử lý

from pathlib import Path


# Bài 0: Đọc dữ liệu từ file data4.txt vào biến danh sách ma_tran.
# Mỗi dòng trong file là một danh sách con và mỗi phần tử phải là số nguyên.
# Đáp án mong đợi:
# ma_tran = [
#     [9, 3, 8, 1, 8, 0, 3, 4, 2, 5],
#     [1, 3, 1, 5, 1, 7, 7, 4, 6, 1],
#     [5, 3, 3, 5, 5, 8, 1, 1, 9, 3],
#     [9, 3, 1, 5, 3, 0, 6, 4, 0, 9],
#     [4, 5, 5, 8, 0, 7, 2, 7, 7, 5],
#     [1, 3, 3, 9, 3, 9, 6, 2, 0, 9],
#     [3, 5, 2, 3, 8, 5, 3, 3, 7, 9],
#     [4, 4, 4, 7, 0, 1, 1, 6, 2, 7],
#     [8, 3, 6, 3, 8, 5, 5, 8, 5, 7],
#     [9, 4, 6, 1, 7, 0, 4, 9, 7, 3]
# ]
duong_dan_file = Path(__file__).with_name("data4.txt")
ma_tran = []

with open(duong_dan_file, "r") as file:
    for dong in file:
        hang = [int(gia_tri) for gia_tri in dong.split()]
        ma_tran.append(hang)


# Bài 1: In toàn bộ ma trận, mỗi hàng trên một dòng và các số cách nhau
# bởi một dấu cách.
# Đáp án mong đợi:
# 9 3 8 1 8 0 3 4 2 5
# 1 3 1 5 1 7 7 4 6 1
# 5 3 3 5 5 8 1 1 9 3
# 9 3 1 5 3 0 6 4 0 9
# 4 5 5 8 0 7 2 7 7 5
# 1 3 3 9 3 9 6 2 0 9
# 3 5 2 3 8 5 3 3 7 9
# 4 4 4 7 0 1 1 6 2 7
# 8 3 6 3 8 5 5 8 5 7
# 9 4 6 1 7 0 4 9 7 3

print("\n* Bài 1:")

pass

# Bài 2: Đếm và in số dòng, số cột của ma trận.
# Code phải đảm bảo vẫn đúng nếu dữ liệu trong file thay đổi.
# Đáp án mong đợi: số dòng = 10, số cột = 10

print("\n* Bài 2:")

pass

# Bài 3: Tính và in tổng của tất cả phần tử trong ma trận.
# Đáp án mong đợi: 449

print("\n* Bài 3:")

pass


# Bài 4: Đếm và in số lượng số chẵn, số lẻ trong ma trận.
# Đáp án mong đợi: có 35 số chẵn, 65 số lẻ

print("\n* Bài 4:")

pass


# Bài 5: Đếm và in số lần số 0 xuất hiện trong ma trận.
# Đáp án mong đợi: 7

print("\n* Bài 5:")

pass

# Bài 6: Đếm và in số lần xuất hiện của mỗi số trong ma trận. 
# Đáp án mong đợi:
# 0 => 7
# 1 => 12
# 2 => 5
# 3 => 18
# 4 => 9
# 5 => 14
# 6 => 6
# 7 => 11
# 8 => 8
# 9 => 10

print("\n* Bài 6:")

pass


# Bài 7: In số thứ tự của dòng có tổng các giá trị lớn nhất.
# Dòng đầu tiên được tính là dòng số 1.
# Đáp án mong đợi: dòng 9 có tổng lớn nhất là 58

print("\n* Bài 7:")

pass
