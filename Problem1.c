
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){

  int sum = 0;
  int limit = atoi(argv[1]);
  
  for(int i = 0; i < limit; i++){
    if((i % 3 == 0) || (i % 5 == 0)){
      sum += i;
    }
  }

  printf("%d\n", sum);

  return 0;
}
