x = int(input())
s = [5, 4, 3, 2, 1]
c = 0

for i in s:
    c += x // i
    x %= i

print(c)