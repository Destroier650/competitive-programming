n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    print(max(0, (y + 99) // 100 - x))
