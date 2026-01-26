s = input()
l = "hello"
fp = 0
r = ""

for i in l:
    for j in range(fp, len(s)):
        if s[j] == i:
            r += s[j]
            fp = j + 1
            break

if r == l:
    print("YES")
else:
    print("NO")