n = int(input())

l = list(map(int, input().split()))

m = []
p = []
pe = []

for i in range(n):
    if l[i] == 1:
        m.append(i)
    elif l[i] == 2:
        p.append(i)
    else:
        pe.append(i)

w = min(len(m), len(p), len(pe))

print(w)

for j in range(w):
    print(m[j] + 1, p[j] + 1, pe[j] + 1)
