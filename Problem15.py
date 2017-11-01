
def combo(n, k):
    return fact(n) / (fact(k) * fact(n-k))

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

if __name__ == '__main__':
    grid_size = 20

    print(combo(40, 20))
