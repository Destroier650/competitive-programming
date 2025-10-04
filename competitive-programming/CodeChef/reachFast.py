n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    print((abs(x - y) + z - 1) // z)