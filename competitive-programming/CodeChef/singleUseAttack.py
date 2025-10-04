n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    print(((x - z) + y - 1) // y + 1)