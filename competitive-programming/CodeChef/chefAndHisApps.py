n = int(input())

for _ in range(n):
    w, x, y, z = map(int, input().split())

    if w - x - y >= z:
        print(0)

    elif w - x >= z or w - y >= z:
        print(1)

    else:
        print(2)