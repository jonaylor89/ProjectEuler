
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_lychrel(num):
    for x in range(50):

        num = num + int(str(num)[::-1])

        if is_palindrome(num):
            return False

    return True

def lychrel(limit):
    total = 0

    for number in range(limit):
        if is_lychrel(number):
            total += 1

    print(total)

if __name__ == '__main__':
    lychrel(10000)
