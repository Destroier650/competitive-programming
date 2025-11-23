n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    l = list(map(int, input().split()))

    if y == 1:
        print("YES" if l == sorted(l) else "NO")
    else:
        print("YES")
