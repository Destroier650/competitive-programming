x = input()

uc = sum(1 for i in x if i.isupper())
dc = sum(1 for i in x if i.islower())

if uc > dc:
    print(x.upper())
else:
    print(x.lower())