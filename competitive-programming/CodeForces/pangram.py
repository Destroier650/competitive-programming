x = int(input())
y = input().lower()

if x >= 26 and len(set(y)) == 26:
    print("YES")
else:
    print("NO")