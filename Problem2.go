
package main

import "fmt"

func main() {
    limit := 4000000
    sum := 0
    a := 1
    b := 0
    
    for a < limit {
        a, b = a + b, a

        if a % 2 == 0 {
            sum = sum + a 
        }
    }

    fmt.Println("Sum:", sum)
}
