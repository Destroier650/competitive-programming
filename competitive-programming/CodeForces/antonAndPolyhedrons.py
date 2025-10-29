x = int(input())
s = 0

for _ in range(x):
    y = input()
    if y == "Icosahedron":
        s += 20
    elif y == "Dodecahedron":
        s += 12
    elif y == "Octahedron":
        s += 8
    elif y == "Cube":
        s += 6
    elif y == "Tetrahedron":
        s += 4

print(s)