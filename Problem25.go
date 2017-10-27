package main

import "fmt"

func fibLimit(limit int) int{

  var a, b int64 = 1, 0
  index := 0

  for IntLen(a) <= limit{
    temp := a
    a = a + b
    b = temp
    index += 1
  }

  return index
}

func IntLen(num int64) int{

  length := 0;

  for num >= 1 {
    num /= 10
    length += 1
  }

  return length
}

func main(){

  fmt.Println(fibLimit(1000))

}
