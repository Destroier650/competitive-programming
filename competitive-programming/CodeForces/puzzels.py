x, y = map(int, input().split())

l = sorted(list(map(int, input().split())))
m = 10**3

for i in range(len(l) - x + 1):
    if l[i + x - 1] - l[i] < m:
        m = l[i + x - 1] - l[i]

print(m)