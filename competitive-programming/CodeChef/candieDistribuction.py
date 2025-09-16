n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if x % y == 0 and (x/y) % 2 == 0:
        print("YES")
    else:
        print("NO")