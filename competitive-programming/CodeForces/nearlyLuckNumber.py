x = input()
s = x.count("4") + x.count("7")
a = {'4', '7'}
if set(str(s)) <= a:
    print("YES")
else:
    print("NO")