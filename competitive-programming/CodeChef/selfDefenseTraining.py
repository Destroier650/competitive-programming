import bisect

n = int(input())

for _ in range(n):
    input()
    l = list(map(int, input().split()))

    print(sum(1 for j in l if 10 <= j <= 60))