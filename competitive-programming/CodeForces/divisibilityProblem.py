x = int(input())

for _ in range(x):
    x, y = map(int, input().split())
    m = x % y
    if m == 0:
        print(m)
    elif x > y:
        print(y - m)
    else:
        print(y - x)