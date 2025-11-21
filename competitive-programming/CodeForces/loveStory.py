n = int(input())

for _ in range(n):
    c = "codeforces"
    x = input()
    d = 0
    for i in range(10):
        if x[i] != c[i]:
            d += 1

    print(d)