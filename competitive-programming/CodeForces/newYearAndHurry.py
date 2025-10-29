x, y = map(int, input().split())
tl = 240 - y
i = 1
sp = 0
while i * 5 <= tl and x - i != -1:
    tl -= i * 5
    sp += 1
    i += 1

print(sp)