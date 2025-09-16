n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if (x + y + 1) % 4 == 1 or (x + y + 1) % 4 == 2:
        print("Alice")

    else:
        print("Bob")