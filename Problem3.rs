
fn is_prime(test: u64) -> bool {
    let calculate_to = (test as f64).sqrt().floor() as u64;

    if test == 1 {
        return false; 
    }

    if test < 4 {
        return true; 
    }

    if test % 2 == 0 {
        return false; 
    }

    if test < 9 {
        return true; 
    }

    if test % 3 == 0 {
        return false; 
    }

    let mut x = 5;

    while x < calculate_to {
        if test % x == 0 {
            return false;
        } 
        if test % (x + 2) == 0 {
            return false; 
        }

        x = x + 6;
    }

    return true;
}

fn main() {
    let number: u64 = 600851475143;
    let end: i32 = (number as f64).sqrt() as i32;
    let mut highest = 0;
    let mut i = 3;

    while i < end{
        if is_prime(i as u64) {
            if number % i as u64 == 0 {
                highest = i; 
            } 
        }

        i = i + 2;
    }

    println!("Highest prime factor {}", highest);
}
