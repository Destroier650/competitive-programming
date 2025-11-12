from collections import Counter

x = input()
y = input()
z = input()

if Counter(x) + Counter(y) == Counter(z):
    print("YES")
else:
    print("NO")
