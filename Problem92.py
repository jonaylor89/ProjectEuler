
def square_digits(num):
    num = str(num)
    new_num = 0

    for letter in num:
        new_num += int(letter)**2

    return new_num

def main(limit):

    total = 0

    cache = {}

    for x in range(1, limit):
        link = x
        while True:

            if link in cache.keys():
                if cache[link] == 89:
                    cache[x] = 89
                    total += 1
                    break
                elif cache[link] == 1:
                    cache[x] = 1
                    break

            if link == 89:
                cache[x] = 89
                total += 1
                break
            elif link == 1:
                cache[x] = 1
                break

            link = square_digits(link)


    print(total)

if __name__ == '__main__':
    main(10000000)
