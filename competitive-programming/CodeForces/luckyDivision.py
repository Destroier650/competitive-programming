s = input()

if set(s).issubset({"4", "7"}):
    print("YES")
else:
    s = int(s)
    if s % 4 == 0 or s % 7 == 0:
        print("YES")
    else:
        print("NO")