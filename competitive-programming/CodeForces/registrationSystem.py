n = int(input())
l = {}

for _ in range(n):
    i = input()
    if i not in l:
        l[i] = 0
        print("OK")
    else:
        l[i] += 1
        print(f"{i}{l[i]}")