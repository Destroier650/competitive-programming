l = sorted(list(map(int, input().split())))
o = ""

for i in range(len(l) - 1):
    o += str(l[3] - l[i]) + " "

print(o)