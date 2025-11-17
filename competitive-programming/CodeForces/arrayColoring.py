n = int(input())

for _ in range(n):
    input()
    l = list(map(int, input().split()))

    ni = 0
    for i in l:
        if i % 2 != 0:
            ni += 1

    if ni % 2 == 0:
        print("YES")
    else:
        print("NO")