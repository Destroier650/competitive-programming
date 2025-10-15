x = []
y = set()

for _ in range(5):
    x.append(int(input()))

for n in x[:4]:
    c = 1
    while (z := n * c) <= x[4]:
        y.add(z)
        c += 1

print(len(y))