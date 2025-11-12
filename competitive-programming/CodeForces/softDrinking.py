n, k, l, c, d, p, nl, np = map(int, input().split())
m = min(k * l / nl, c * d, p / np) // n
print(int(m))