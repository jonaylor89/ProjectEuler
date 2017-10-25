
#include <stdio.h>
#include <math.h>

int main(){

  int isPrime;
  unsigned long sum = 5;

  for(int i = 5; i < 2000000; i += 2){

    isPrime = 1;

    for(int j = 3; j < round(sqrt(i))+1; j += 2){
      if(i % j == 0){
        isPrime = 0;
        break;
      }
    }

    if(isPrime == 1){
      sum += i;
    }


  }

  printf("%lu\n", sum);

  return 0;
}
