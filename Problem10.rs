
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

    while x <= calculate_to {
        if test % x == 0 {
            return false;
        } 
        if test % (x + 2) == 0 {
            return false; 
        }

        x += 6;
    }

    return true;
}

fn main() {
    let limit = 2000000;
    let mut sum: u64 = 5;

    let mut x = 5;
    while x <= limit {
        if is_prime(x) {
            sum += x; 
        }
        x += 2;

        if x <= limit && is_prime(x) {
            sum += x; 
        }

        x += 4
    }

    println!("Sum: {}", sum)
}
