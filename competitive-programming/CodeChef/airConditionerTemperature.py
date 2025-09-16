n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    if a <= b and b >= c:
        print("YES")
    else:
        print("NO")