
def fib(limit):
    a, b = 1, 0

    while a < limit:
        a, b = a+b, a
        yield a


if __name__ == '__main__':
    even_list = (x for x in fib(4000000) if x%2 == 0)
    print(sum(even_list))
