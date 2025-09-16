n = int(input())

for _ in range(n):
    a, b, x, y = map(int, input().split())

    if a <= b <= a+x or a >= b >= a - y:
        print("YES")
    else:
        print("NO")