n = int(input())

md = 0
p1 = 0
p2 = 0
w = 0

for _ in range(n):
    x, y = map(int, input().split())
    p1 += x
    p2 += y

    if p1 > p2 and p1 - p2 > md:
        md = p1 - p2
        w = 1

    elif p2 - p1 > md:
        md = p2 - p1
        w = 2

print(w, md)
