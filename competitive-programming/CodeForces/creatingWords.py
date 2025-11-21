n = int(input())

for _ in range(n):
    x, y = input().split()

    print(y[0] + x[1:], x[0] + y[1:])