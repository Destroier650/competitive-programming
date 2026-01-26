s = input()
c = 1

for i in range(len(s) - 1):
    l = s[i]
    if l == s[i + 1]:
        c += 1
    else:
        c = 1
    if c == 7:
        break

if c == 7:
    print("YES")
else:
    print("NO")
