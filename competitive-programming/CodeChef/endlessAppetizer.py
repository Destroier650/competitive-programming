n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    print(((x + z // 30) + y - 1) // y)