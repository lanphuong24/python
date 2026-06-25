## Tách xâu (split)

# Nhập vào một câu, đếm số từ trong câu đó
# vd: "Tin học rất thú vị" => 5 từ

print("Nhập một câu:")
s = input()

word = s.split(" ")
wordCount = len(word)



print(f"Số từ trong câu: {wordCount}")
