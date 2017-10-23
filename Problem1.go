
package main;

import "fmt"

func main(){

  limit := 1000
  sum := 0

  for i := 0; i < limit; i++ {
    if i % 5 == 0 || i % 3 == 0 {
      sum = sum + i
    }
  }

  fmt.Println(sum)

}
