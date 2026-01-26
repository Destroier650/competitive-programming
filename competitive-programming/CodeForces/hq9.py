s = set(input())

if any(c in s for c in "HQ9"):
    print("YES")
else:
    print("NO")