x = int(input())
s = 0
c = [1, 5, 10, 20, 100]

for n in c[::-1]:
    s += x // n
    x %= n

print(s)