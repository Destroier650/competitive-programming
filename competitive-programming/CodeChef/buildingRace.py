n = int(input())

for _ in range(n):
    a, b, x, y = map(int, input().split())

    if a / x < b / y:
        print("Chef")

    elif a / x > b / y:
        print("Chefina")

    else:
        print("Both")