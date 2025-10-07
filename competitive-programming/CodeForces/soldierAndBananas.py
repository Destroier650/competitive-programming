x, y, z = map(int, input().split())
s = -y

for i in range(z + 1):
    s += x * i

print(max(0, s))