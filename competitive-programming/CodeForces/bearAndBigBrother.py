x, y = map(int, input().split())

a = 0

while x <= y:
    x *= 3
    y *= 2
    a += 1

print(a)