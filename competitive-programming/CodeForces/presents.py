input()
l = list(map(int, input().split()))
i = ""

for n in sorted(l):
    i += str(l.index(n) + 1) + " "

print(i)