input()
x = input()
a = x.count("A")
t = len(x) / 2
if a > t:
    print("Anton")
elif a < t:
    print("Danik")
else:
    print("Friendship")