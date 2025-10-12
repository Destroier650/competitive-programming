x = int(input())
s = ""
for n in range(x):
    s = s.replace("it", "that")
    if (n + 1) % 2 != 0:
        s += " I hate it"
    else:
        s += " I love it"

print(s.strip())