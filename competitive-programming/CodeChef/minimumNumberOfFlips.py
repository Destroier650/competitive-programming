n = int(input())

for _ in range(n):
    input()
    l = list(map(int, input().split()))

    if len(l) % 2 != 0:
        print(-1)
    else:
        print(abs(sum(l)) // 2)