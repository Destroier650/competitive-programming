n = int(input())

for _ in range(n):
    input()
    l = list(map(int, input().split()))
    s = True
    
    for i in range(len(l) - 1):
        if abs(l[i] - l[i + 1]) > 1:
            s = False
            break

    if s:
        print("YES")
    else:
        print("NO")
