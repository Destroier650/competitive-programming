input()
l = sorted(list(map(int,input().split())))
print("".join(str(c) + " " for c in l))