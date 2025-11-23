n = int(input())

for _ in range(n):
    x = input()
    s = ""
    for i in range(len(x) // 2):
        s += x[i * 2]
    print(s + x[-1])