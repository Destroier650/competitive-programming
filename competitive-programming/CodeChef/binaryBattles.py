import math

n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    nor = int(math.log(x, 2))
    print(nor * y + (nor - 1) * z)