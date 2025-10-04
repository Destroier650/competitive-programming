def is_prime(n):
    if n < 2:
        return "yes"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "no"
    return "yes"

n = int(input())

for _ in range(n):
    x = int(input())

    print(is_prime(x))