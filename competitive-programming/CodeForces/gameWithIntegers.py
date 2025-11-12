n = int(input())

for _ in range(n):
    x = int(input())
    print("First") if x % 3 != 0 else print("Second")