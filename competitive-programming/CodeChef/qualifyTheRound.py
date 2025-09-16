n = int(input())

for i in range(n):
    x, a, b = map(int, input().split())

    if x <= a + b * 2:
        print("Qualify")

    else:
        print("NotQualify")