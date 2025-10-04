n = int(input())

for _ in range(n):
    l = list(map(int, input().split()))
    a = l[0:3]
    b = l[3:6]

    if sum(a) - min(a) > sum(b) - min(b):
        print("Alice")
    elif sum(a) - min(a) < sum(b) - min(b):
        print("Bob")
    else:
        print("Tie")