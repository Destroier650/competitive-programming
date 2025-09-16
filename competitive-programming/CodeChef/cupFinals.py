n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    if abs(x - y) <= z:
        print("YES")

    else:
        print("NO")