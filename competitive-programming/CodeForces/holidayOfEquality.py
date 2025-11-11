input()

l = list(map(int, input().split()))

m = max(l)
s = 0

for n in l:
    s += m - n

print(s)