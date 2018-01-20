
package main

import "math"
import "fmt"

func is_prime(test int) bool {
    calculate_to := int(math.Sqrt(float64(test)))

    if test == 1 {
        return false 
    }

    if test < 4 {
        return true 
    }

    if test % 2 == 0 {
        return false 
    }

    if test < 9 {
        return true 
    }

    if test % 3 == 0 {
        return false 
    }

    x := 5

    for x < calculate_to {
        if test % x == 0 {
            return false 
        }
        if test % (x + 2) == 0 {
            return false 
        }

        x = x + 6
    }

    return true
}

func main() {
    number := 600851475143
    end := int(math.Sqrt(float64(number)))
    highest := 0
    x := 3

    for x < end {
        if is_prime(x) {
            if number % x == 0 {
                highest = x 
            } 
        } 

        x = x + 2
    }

    fmt.Println("Highest", highest)

}
