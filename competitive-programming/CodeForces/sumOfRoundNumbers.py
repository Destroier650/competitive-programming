x = int(input())

for _ in range(x):
    y = input()
    z = ""
    s = 0
    for n in range(len(y)):
        if y[n] != "0":
            z += y[n] + "0" * (len(y) - n - 1) + " "
            s += 1
    print(s)
    print(z)