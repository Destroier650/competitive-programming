n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())

    if y * 3 - (x - y) >= z:
        print("PASS")

    else:
        print("FAIL")