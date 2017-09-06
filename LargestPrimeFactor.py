

"""

This is super slow.
Don't ever use this 

"""


import math

factors = set()

def isPrime(p):

    if p == 3 or p == 2 or p == 1: #Fuck it, for this "1" will be prime
        return True

    if p % 2 == 0:
        return False

    sqrt_p = math.sqrt(p)

    for n in range(3, int(sqrt_p) + 1, 2):
        if p % n == 0:
            return False

    return True


def factorize(n):
    global factors

    if isPrime(n):
        factors.add(n)
    else:
        for f in range(2, n):
            if n % f == 0:
                factorize(n // f)
                factorize(f)


if __name__ == '__main__':
    n = 600851475143
    factorize(n)
    print(max(factors))
