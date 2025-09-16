n = int(input())

for _ in range(n):
    x = int(input())

    if x % 5 != 0:
        print(-1)

    else:
        print(x // 10 + (x % 10) // 5)
