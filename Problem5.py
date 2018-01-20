
def main(limit):

    smallest_number = 0
    product_of_primes = 2 * 3 * 7 * 11 * 13 * 17 * 19

    while True:

        smallest_number += product_of_primes

        for i in range(1, limit+1):
            if smallest_number % i != 0:
                break
        else:
            print(smallest_number)
            return


if __name__ == '__main__':
    main(20)
