n = int(input())

for _ in range(n):
    x = int(input())
    y = input()
    a = 0

    for i in range(x // 2):
        if y[i] != y[x - 1 - i]:
            a += 1
        else:
            break
    print(x - a * 2)