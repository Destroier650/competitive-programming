from fractions import Fraction

x, y = map(int, input().split())

m = max(x, y)
f = Fraction(7 - m, 6)
print(f"{f.numerator}/{f.denominator}")