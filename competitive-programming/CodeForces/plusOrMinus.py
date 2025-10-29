n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    if x + y == z:
        print("+")
    else:
        print("-")