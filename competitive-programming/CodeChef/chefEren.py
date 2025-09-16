n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    even = x // 2
    odd = x - even

    print(even * y + odd * z)