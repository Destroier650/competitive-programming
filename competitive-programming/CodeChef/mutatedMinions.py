n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    l = list(map(int, input().split()))

    print(sum(1 for n in l if (n + y) % 7 == 0))