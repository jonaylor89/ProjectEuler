
def d(num):

    factors = []

    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return sum(factors)

def main(limit):
    amicable_numbers = set()

    for i in range(1, limit):
        ami = d(i)

        if d(ami) == i and ami != i:
            amicable_numbers.add(ami)
            amicable_numbers.add(i)


    print(sum(amicable_numbers))

if __name__ == '__main__':
    main(10000)
