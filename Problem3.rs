
fn isPrime(test: u64) -> bool {
    let calculateTo = (test as f64).sqrt() as u64;

    for x in (3..calculateTo).step_by(6) {
        if test % x == 0 {
            return false;
        } 
    }

    return true;
}

fn main() {
    let NUMBER: u64 = 600851475143;
    let END: i32 = (NUMBER as f64).sqrt() as i32;
    let mut highest = 0;

    for i in (3..END).step_by(6) {
        if isPrime(i as u64) {
            if NUMBER % i as u64 == 0 {
                highest = i; 
            } 
        }
    }

    println!("Highest prime factor {}", highest);
}
