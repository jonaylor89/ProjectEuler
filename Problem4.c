
#include <stdio.h>

int isPalindrome(int question) {
    int reverseNum = 0;
    int input = question;

    while(input != 0){
        reverseNum = reverseNum * 10 + input % 10;
        input = input / 10;
    }

    return question == reverseNum;
}

int main() {
    int max = 0;
    int sum;

    for(int i = 100; i < 999; i++) {
        for(int j = 100; j < 999; j++) {
            sum = i * j;
            if(isPalindrome(sum) && sum > max) {
                max = sum; 
            }
        }
    }

    printf("Sum: %d\n", max);
}
