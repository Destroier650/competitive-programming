input()

x = list(map(int, input().split()))
min = x[0]
max = x[0]
s = 0

for i in range(len(x)):
    if x[i] > max and i != 0:
        max = x[i]
        s += 1
    elif x[i] < min and i != 0:
        min = x[i]
        s += 1

print(s)