
def sum_multiples_3_and_5(limit):
    value_list = [x for x in range(limit) if (x%5 == 0 or x%3 == 0)]
    answer = sum(value_list)
    return answer


if __name__ == '__main__':
    print(sum_multiples_3_and_5(1000))
