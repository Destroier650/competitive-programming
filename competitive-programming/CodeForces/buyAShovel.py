x, y = map(int, input().split())
i = 1

while i * x % 10 != 0 and i * x % 10 - y != 0:
    i += 1

print(i)