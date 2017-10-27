
amicable_numbers = set()

def d(num):

    factors = []

    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return sum(factors)


if __name__ == '__main__':
    for i in range(1, 10000):
        ami = d(i)

        if d(ami) == i and ami != i:
            amicable_numbers.add(ami)
            amicable_numbers.add(i)


    print(sum(amicable_numbers))
