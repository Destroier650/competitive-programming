n = int(input())

for _ in range(n):
    l = sorted(list(map(int, input().split())))
    if len(l) % 2 != 0:
        print(l[len(l) // 2])
    else:
        print((l[len(l) // 2] + l[len(l) // 2 + 1]) / 2)