n = int(input())

for _ in range(n):
    l = list(map(int, input().split()))

    x = y = 0

    for n in l:
        if n > x:
            y = x
            x = n
        elif n > y:
            y = n

    print(x + y)