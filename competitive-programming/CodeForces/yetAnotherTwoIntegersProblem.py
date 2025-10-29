n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    d = max(x, y) - min(x, y)
    print(d // 10 + (1 if d % 10 != 0 else 0))
