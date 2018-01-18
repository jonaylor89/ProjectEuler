
fn main() {
    let limit = 4000000;
    let mut sum = 0;
    let mut a = 1;
    let mut b = 0;
    let mut temp;

    while a < limit {
        temp = a;
        a = a + b;
        b = temp;

        if a % 2 == 0 {
            sum = sum + a; 
        }
    }

    println!("Sum: {}", sum)
}
