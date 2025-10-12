x = input()
y = input()

s = ""
for n in range(len(x)):
    if x[n] != y[n]:
        s += "1"
    else:
        s += "0"

print(s)