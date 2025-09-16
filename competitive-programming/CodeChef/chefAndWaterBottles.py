n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    print(min(x, z // y))