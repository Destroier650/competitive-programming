m, n, a = map(int, input().split())

s = ((m + a - 1) // a) * ((n + a - 1) // a)
print(s)