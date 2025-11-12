input()

c = list(map(int, input().split()))

l = 0
r = len(c) - 1
s = 0
d = 0
for i in range(len(c)):
    if c[l] >= c[r]:
        slc = c[l]
        l += 1
    else:
        slc = c[r]
        r -= 1

    if i % 2 == 0:
        s += slc
    else:
        d += slc

print(f"{s} {d}")