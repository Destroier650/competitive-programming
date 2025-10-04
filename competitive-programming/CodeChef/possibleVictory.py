x, y, z = map(int, input().split())

if x < 720 and x < (20 - y) * 36 + z:
    print("YES")
else:
    print("NO")