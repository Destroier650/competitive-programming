n, l = map(int, input().split())

a = sorted(list(map(int, input().split())))
m = max(a[0], l - a[-1])

for i in range(len(a) - 1):
    if (a[i+1] - a[i]) / 2 > m:
        m = (a[i+1] - a[i]) / 2

print(m)