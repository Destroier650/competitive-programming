x = int(input())

s = 0
for _ in range(x):
    y, z = map(int, input().split())
    if y + 2 <= z:
        s+= 1

print(s)
