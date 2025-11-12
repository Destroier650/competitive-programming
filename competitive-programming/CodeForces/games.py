x = int(input())
l = []
s = 0

for _ in range(x):
    x, y = input().split()
    l.append({'x': x, 'y': y})

for i in range(len(l)):
    for n in range(len(l)):
        if l[i]['x'] == l[n]['y']:
            s += 1

print(s)
