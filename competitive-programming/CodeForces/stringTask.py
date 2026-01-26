s = input().lower()
r = "aeiouy"
a = ""

for l in s:
    if l not in r:
        a += "." + l
print(a)