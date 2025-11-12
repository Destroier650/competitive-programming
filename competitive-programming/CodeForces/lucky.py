n = int(input())

for _ in range(n):
    x = input()
    fh = 0
    sh = 0
    for c in range(len(x) // 2):
        fh += int(x[c])

    for c in range(len(x) // 2, len(x)):
        sh += int(x[c])

    if fh == sh:
        print("YES")
    else:
        print("NO")