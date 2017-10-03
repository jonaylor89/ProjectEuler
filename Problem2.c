
#include <stdio.h>

int main(){

  long limit = 4000000;
  long sum = 0;

  int a = 1;
  int b = 0;
  int temp;

  while(a < limit){
    temp = a;
    a = a + b;
    b = temp;

    if(a % 2 == 0){
      sum += a;
    }
  }

  printf("%d\n", sum);

  return 0;
}
