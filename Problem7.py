
def create_primes(limit):
    primes = [2]
    n = 3
    while len(primes) < limit:
        for prime in primes:
            if n%prime == 0:
                break
        else:
            primes.append(n)

        n += 2

    return primes


if __name__ == '__main__':
    answer = create_primes(10001)[-1]
    print(answer)
