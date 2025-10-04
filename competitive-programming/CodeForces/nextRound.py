x, y = map(int, input().split())

l = list(map(int, input().split()))
k = l[y-1]
c = 0

for n in l:
    if n > 0 and n >= k:
        c += 1

print(c)
