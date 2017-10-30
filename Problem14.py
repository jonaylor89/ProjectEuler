
from concurrent.futures import ThreadPoolExecutor

def collatz_length(num):

    items = 1

    while num > 1:

        items += 1

        if num % 2 == 0:
            num = num / 2

        else:
            num = 3 * num + 1

    return items

def collatz_max(d):

    winner = 0
    max_length = 1

    for k, v in d:

        if v > max_length:
            winner = k
            max_length = v

    return winner

if __name__ == '__main__':

    limit = 1000000

    with ThreadPoolExecutor(max_workers=1000) as executor:
        iterable = executor.map(collatz_length, range(1, limit))

    sequences = zip(range(1, limit), iterable)

    print(collatz_max(sequences))
