n = int(input())

for _ in range(n):
    x, y, a, b = map(int, input().split())

    print(len({x, y} - {a, b}))