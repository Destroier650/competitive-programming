n = int(input())

for _ in range(n):
    input()
    x = list(map(int, input().split()))

    for j in range(len(x)):
        if len(x) == 1:
            print(0)

        elif abs(x[len(x) - j - 1]) > 0:
            print(len(x) - j - 1)
            break
