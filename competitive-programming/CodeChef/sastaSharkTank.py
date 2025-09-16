n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    y /= 2
    if x > y:
        print("FIRST")
    elif x < y:
        print("SECOND")
    else:
        print("ANY")