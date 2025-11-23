n = int(input())
r = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        r += 1
    elif x < y:
        r -= 1

if r > 0:
    print("Mishka")
elif r < 0:
    print("Chris")
else:
    print("Friendship is magic!^^")