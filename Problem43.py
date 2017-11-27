
import numpy as np

def pandigital_generator():

    the_range = np.arange(10)

    for a in the_range:
        for b in np.delete(the_range, a):
            for c in np.delete(the_range, [a, b]):
                for d in np.delete(the_range, [a, b, c]):
                    for e in np.delete(the_range, [a, b, c, d]):
                        for f in np.delete(the_range, [a, b, c, d, e]):
                            for g in np.delete(the_range, [a, b, c, d, e, f]):
                                for h in np.delete(the_range, [a, b, c, d, e, f, g]):
                                    for i in np.delete(the_range, [a, b, c, d, e, f, g, h]):
                                        for j in np.delete(the_range, [a, b, c, d, e, f, g, h, i]):
                                            yield str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i)


def main():

    somme = 0

    for pandigit in pandigital_generator():
        num_string = pandigit

        premier = int(num_string[1:5]) % 2 == 0
        deuxieme = int(num_string[2:6]) % 3 == 0
        troisieme = int(num_string[3:7]) % 5 == 0
        quatrieme = int(num_string[4:8]) % 7 == 0
        cinquieme = int(num_string[5:9]) % 11 == 0
        sixieme = int(num_string[6:10]) % 13 == 0
        septieme = int(num_string[7:11]) % 17 == 0

        if all([premier, deuxieme, troisieme, quatrieme, cinquieme, sixieme, septieme]):
            somme += pandigit

    print(somme)

if __name__ == '__main__':
    main()
