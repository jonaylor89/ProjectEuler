
from SpeedTesting import clock

@clock(results='show')
def create_primes(limit):
    primes = [2]

    for n in range(3, limit, 2):

        possible_divisors = (x for x in primes if x <= n**(0.5))

        for prime in possible_divisors:
            if n%prime == 0:
                 break
        else:
            primes.append(n)

    return primes

if __name__ == '__main__':
    answer = sum(create_primes(2000000))
    print(answer)

    # for x in range(10, 100000, 1000):
    #     create_primes(x)
