
def fib(limit):
    a, b = 1, 0
    index = 0
    while len(str(a)) < limit:
        a, b = a+b, a
        index += 1
    else:
        return (index+1, len(str(a)))

if __name__ == '__main__':
    answer = fib(20000)
    print(answer[0])
