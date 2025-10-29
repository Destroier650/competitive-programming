x = int(input())

for _ in range(x):
    z, y, a = map(int, input().split())

    if z == y + a or y == z + a or a == z + y:
        print("YES")
    else:
        print("NO")