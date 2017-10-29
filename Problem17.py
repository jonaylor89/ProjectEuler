
def translate_ones(ones):

    translation = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine"
    }

    return translation[ones]

def translate_tens(tens):

    teens = {
        00 : "",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen"
    }

    if tens < 20:
        tens_place = teens[tens]

    elif tens < 30:
        tens_place = "twenty" + translate_ones(tens%10)

    elif tens < 40:
        tens_place = "thirty" + translate_ones(tens%10)

    elif tens < 50:
        tens_place = "forty" + translate_ones(tens%10)

    elif tens < 60:
        tens_place = "fifty" + translate_ones(tens%10)

    elif tens < 70:
        tens_place = "sixty" + translate_ones(tens%10)

    elif tens < 80:
        tens_place = "seventy" + translate_ones(tens%10)

    elif tens < 90:
        tens_place = "eighty" + translate_ones(tens%10)

    elif tens < 100:
        tens_place = "ninety" + translate_ones(tens%10)

    else:
        tens_place = "Something has gone astray in the tens function"

    return tens_place


def translate_hundreds(hundreds):

    if hundreds % 100 == 0:
        hundreds_place = translate_ones(hundreds//100) + "hundred"

    elif hundreds % 100 < 10:
        hundreds_place = translate_ones(hundreds//100) + "hundredand"  + translate_ones(hundreds%10)

    elif hundreds % 100 < 100:
        hundreds_place = translate_ones(hundreds//100) + "hundredand"  + translate_tens(hundreds%100)

    else:
        hundreds_place = "print something is astray in hundreds function"

    return hundreds_place


def translate_thousands(thousands):

        if thousands//1000 < 10:
            thousands_place = translate_ones(thousands//1000)

        elif thousands//1000 < 100:
            thousands_place = translate_tens(thousands//1000)

        elif thousands//1000 < 1000:
            thousands_place = translate_hundreds(thousands//1000)

        else:
            print("Something has gone in the thousands function")

        if thousands%1000 < 10:
            last_part = translate_ones(thousands%1000)

        elif thousands%1000 < 100:
            last_part = translate_tens(thousands%1000)

        elif thousands%1000 < 1000:
            last_part = translate_hundreds(thousands%1000)

        else:
            print("Something has gone astray in second part of thousands functions")

        return thousands_place + "thousand" + last_part

def num_to_string(number):

    word = ""

    if number < 10:
        word = translate_ones(number)

    elif number < 100:
        word = translate_tens(number)

    elif number < 1000:
        word = translate_hundreds(number)

    elif number < 1000000:
        word = translate_thousands(number)

    else:
        print("Something has gone astray")

    return word



if __name__ == '__main__':

    total = 0

    for i in range(1001):
        total += len(num_to_string(i))

    print(total)
