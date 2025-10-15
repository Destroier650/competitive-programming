x = int(input())
y = list(map(int, input().split()))

iMin = len(y) - 1 - y[::-1].index(min(y))
iMax = y.index(max(y))

if iMin < iMax:
    print(iMax + len(y) - iMin - 2)
else:
    print(iMax + len(y) - iMin - 1)