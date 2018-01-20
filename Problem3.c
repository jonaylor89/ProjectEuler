
#include <stdio.h>
#include <math.h>

#define NUMBER 600851475143

int isPrime(int test) {
    int calculateTo = ( (int) floor(sqrt(test)) );

    if(test == 1) {
        return 0; 
    }

    if(test < 4) {
        return 1; 
    }

    if(test % 2 == 0) {
        return 0; 
    }

    if(test < 9) {
        return 1; 
    }

    if(test % 3 == 0) {
        return 0; 
    }

    for(int i = 5; i <= calculateTo; i += 2) {
        if(test % i == 0) {
            return 0; 
        }
        if(test % (i + 2) == 0) {
            return 0; 
        }
    }

    return 1;
}

int main() {
    int highest = 0;

    for(int i = 3; i <= floor(sqrt(NUMBER)); i += 2) {
        if(isPrime(i)) {
            if(NUMBER % i == 0)
                highest = i;
        }

    }

    printf("%d", highest);
    
    return 0;

}
