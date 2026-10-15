reader = open("algo/search/bt1.inp", "r")
writer = open("algo/search/bt1.out", "w")
list = []
for line in reader:
    list.append(int(line))
reader.close()

for num in list:
    print(num + 1, file=writer)
writer.close()

