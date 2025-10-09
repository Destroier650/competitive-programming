x = int(input())

while True:
    x += 1
    if len(set(str(x))) == 4:
        print(x)
        break
        