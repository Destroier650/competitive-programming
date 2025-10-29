input()
x = list(map(int,input().split()))
s = 0
c = 0
for i in x:
    if i < 0 and c == 0:
        s += 1

    elif i < 0 and c != 0:
        c -= 1

    elif i > 0:
        c += i
print(s)