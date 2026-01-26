x, y = map(int, input().split())

c = (x + 1) // 2

if y <= c:
    print(2 * y - 1)
else:
    print(2 * (y - c))