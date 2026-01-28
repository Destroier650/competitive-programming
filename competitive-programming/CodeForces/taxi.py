n = int(input())
l = list(map(int, input().split()))

g1 = l.count(1)
g2 = l.count(2)
g3 = l.count(3)
g4 = l.count(4)

taxis = g4 + g3 + g2 // 2

g1 = max(0, g1 - g3)

if g2 % 2 != 0:
    taxis += 1
    g1 = max(g1 - 2, 0)

taxis += (g1 + 3) // 4

print(taxis)