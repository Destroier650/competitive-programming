n = int(input())
s = 0
for _ in range(n):
    x = input().count("1")
    if x >= 2:
        s += 1

print(s)