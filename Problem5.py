
def main(limit):

    smallest_number = 0

    while True:

        smallest_number += 2

        for i in range(1, limit+1):
            if smallest_number % i != 0:
                break
        else:
            print(smallest_number)
            return


if __name__ == '__main__':
    main(20)
