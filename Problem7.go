
package main

import "fmt"

func CreatePrimes(limit int) []int{

  primes := []int{2, 3}
  n := 3

  for len(primes) < limit {

    isPrime := true

    for _, element := range primes{
      if n % element == 0 {
        isPrime = false
        break
      }
    }

    if isPrime {
      primes = append(primes, n)
    }

    n = n + 2

  }

  return primes

}

func main(){

  PrimeArray := CreatePrimes(10001)
  //fmt.Println(PrimeArray)
  fmt.Println(PrimeArray[len(PrimeArray)-1])

}
