input()
x = input()
count = 0

for i in range(len(x)-1):
    if x[i:i+2] == "RR":
        count += 1
    elif x[i:i+2] == "GG":
        count += 1
    elif x[i:i + 2] == "BB":
        count += 1

print(count)