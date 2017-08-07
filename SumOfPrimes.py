
from SpeedTesting import speed

@speed
def create_primes(limit):
    primes = [2]
    n = 3
    while n < limit:

        possible_divisors = (x for x in primes if x <= n**(0.5))

        for prime in possible_divisors:
            if n%prime == 0:
                 break
        else:
            primes.append(n)
        n += 2

    return primes

if __name__ == '__main__':
    answer = sum(create_primes(20000))
    print(answer)

    # for x in range(10, 100000, 1000):
    #     create_primes(x)
