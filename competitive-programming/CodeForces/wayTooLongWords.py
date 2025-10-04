n = int(input())

for _ in range(n):
    x = input()

    if len(x) <= 10:
        print(x)

    else:
        print(f"{x[0]}{len(x)-2}{x[-1]}")