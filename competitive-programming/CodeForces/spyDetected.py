n = int(input())

for _ in range(n):
    input()
    l = list(map(int, input().split()))
    m, M = min(l), max(l)

    if l.count(m) == 1:
        print(l.index(m) + 1)
    else:
        print(l.index(M) + 1)