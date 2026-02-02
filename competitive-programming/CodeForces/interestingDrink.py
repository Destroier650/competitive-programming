import bisect

input()

l = sorted(list(map(int, input().split())))
n = int(input())

for i in range(n):
    x = int(input())
    print(bisect.bisect_right(l, x))