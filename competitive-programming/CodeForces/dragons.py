s, n = map(int, input().split())

dl = []

for _ in range(n):
    x, y = map(int, input().split())
    dl.append((x, y))

dl = sorted(dl)

for k, v in dl:
    if k >= s:
        s = -1
        break
    else:
        s += v

if s == -1:
    print("NO")
else:
    print("YES")