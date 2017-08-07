

palindrome_list = [i * j for i in range(100, 999) for j in range(100, 999) if(str(i*j) == str(i*j)[::-1])]

if __name__ == '__main__':
    print(max(palindrome_list))
