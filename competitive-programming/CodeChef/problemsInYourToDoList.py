n = int(input())

for i in range(n):
    input()
    x = list(map(int, input().split()))
    counter = 0
    for n in x:
        if n >= 1000:
            counter += 1
    print(counter)