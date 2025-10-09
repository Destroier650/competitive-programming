x = int(input())
lm = ""
s = 0
for _ in range(x):
    y = input()
    if lm == "" or lm[1] == y[0]:
        s += 1
    lm = y

print(s)