n = int(input())
l = list(map(int, input().split()))
o = 0
o_idx = 0
e = 0
e_idx = 0

for i in range(len(l)):
    if l[i] % 2 == 0:
        o += 1
        o_idx = i

    else:
        e += 1
        e_idx = i

    if o > 1 and e == 1:
        print(e_idx + 1)
        break
    elif e > 1 and o == 1:
        print(o_idx + 1)
        break