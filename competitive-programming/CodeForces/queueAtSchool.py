x, y = map(int, input().split())
z = input()
for _ in range(y):
    if "BG" in z:
        z = z.replace("BG", "GB")
print(z)