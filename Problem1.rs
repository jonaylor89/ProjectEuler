
fn main() {
    
    let limit = 1000;
    let mut sum = 0;

    for x in 1..limit {
        if x % 3 == 0 || x % 5 == 0 {
            sum = sum + x; 
        } 
    }

    println!("Sum is: {}", sum);
}
