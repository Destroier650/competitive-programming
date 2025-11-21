n = int(input())

for _ in range(n):
    l = 0
    ml = 0

    input()
    x = list(map(int, input().split()))

    for i in x:
        if i == 0:
            l += 1
            if ml < l:
                ml = l
        else:
            l = 0

    print(ml)