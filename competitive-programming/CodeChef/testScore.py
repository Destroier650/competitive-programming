n = int(input())

for i in range(n):
    x, y, z = map(int, input().split())

    if z == 0:
        print("YES")
    else:
        if z % y == 0 and z // y <= x:
            print("YES")
        else:
            print("NO")
