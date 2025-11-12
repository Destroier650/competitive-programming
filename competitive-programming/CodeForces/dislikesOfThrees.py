n = int(input())

for _ in range(n):
    x = int(input())
    l = 0
    c = 0
    while c < x:
        l += 1
        if l % 10 != 3 and l % 3 != 0:
            c += 1

    print(l)