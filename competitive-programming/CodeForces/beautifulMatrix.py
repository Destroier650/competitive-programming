m = []
row_containing_one = 0
index_one = 0
for n in range(5):
    x = list(input().split())
    m.append(x)
    if x.count("1") > 0:
        row_containing_one = n
        index_one = x.index("1")
print(abs(row_containing_one - 2) + abs(index_one - 2))