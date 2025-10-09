n = int(input())
s = 0
mc = 0
for _ in range(n):
    x, y = map(int, input().split())
    s = s - x + y
    if s > mc:
        mc = s

print(mc)