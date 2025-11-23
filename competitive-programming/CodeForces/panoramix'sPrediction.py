n, m = map(int, input().split())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

i = primes.index(n)

if i == len(primes) - 1:
    print("NO")
else:
    print("YES" if primes[i + 1] == m else "NO")

n, m = map(int,input().split())
"""
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

p = n + 1
while not is_prime(p):
    p += 1

print("YES" if p == m else "NO")"""