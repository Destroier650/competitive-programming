s = input()

if s[1::].upper() == s[1::] and s[0].islower():
    print(s.capitalize())

elif s.upper() == s:
    print(s.lower())
else:
    print(s)