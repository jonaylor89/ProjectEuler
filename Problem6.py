

def main(limit):

    sum_of_squares = sum(x**2 for x in range(limit+1))

    square_of_sum = sum(x for x in range(limit+1))**2

    print(square_of_sum - sum_of_squares)




if __name__ == '__main__':
    main(100)
