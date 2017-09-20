
productList = set()


def addProducts(num):

    for x in range(len(num) - 12):
        sum = int(num[x])
        for y in range(1, 13):
            sum = sum * int(num[x + y])
            productList.add(sum)


def main():

    large_string = "7316717653133062491922511967442657474235534919493\
496983520312774506326239578318016984801869478851843\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"


    addProducts(large_string)


    print(max(productList))


if __name__ == "__main__":
    main()
