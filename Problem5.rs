
fn main() {
    let limit = 20;
    let sum_of_primes = 2 * 3 * 11 * 13 * 17 * 19;
    let mut complete;
    let mut smallest_number = 0;

    loop {
 
        smallest_number += sum_of_primes;

        complete = 0;

        for i in 1..(limit+1) {
            if smallest_number % i != 0 {
                break; 
            } else {
                complete += 1; 
            } 
        }

        if complete == limit{
            break; 
        }
    }

    println!("Smallest Number: {}", smallest_number)
}
