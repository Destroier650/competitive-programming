n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    l = list(map(int, input().split()))
    counter = 0
    for j in l:
        if j >= b:
            counter += 1
    print(counter)