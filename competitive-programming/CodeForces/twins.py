n = int(input())
s = sorted(list(map(int, input().split())))
s_sum = sum(s)
r_sum = 0
indx = 0

for i in reversed(s):
    r_sum += i
    if r_sum > s_sum / 2:
        print(indx + 1)
        break
    else:
        indx += 1