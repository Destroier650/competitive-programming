n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    sum = x + y
    if sum >= 11:
        print(21 - sum)
    else:
        print(-1)