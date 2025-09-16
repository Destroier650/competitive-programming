import math

n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    print(math.ceil(x / (y * z)))