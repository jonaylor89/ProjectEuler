
def pythagorean_theorem(a, b, c):
    return a**2 + b**2 == c**2

def main(limit):
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if a + b + c == limit:
                    if pythagorean_theorem(a, b, c):
                        print(a, b, c)
                        print(a * b * c)
                        return


if __name__ == '__main__':
    main(1000)
