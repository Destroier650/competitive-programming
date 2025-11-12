x = int(input())

for _ in range(x):
    y = int(input())
    if y >= 1900:
        print("Division 1")
    elif 1899 >= y >= 1600:
        print("Division 2")
    elif 1599 >= y >= 1400:
        print("Division 3")
    else:
        print("Division 4")