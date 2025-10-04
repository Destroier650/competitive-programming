n = int(input())
s = 0
for _ in range(n):
    x = input()
    s += x.count("++") - x.count("--")

print(s)