
fn pythagorean_theorem(a: i32, b: i32, c: i32) -> bool {
    return a.pow(2) + b.pow(2) == c.pow(2);
}

fn main() {
    let limit = 1000;

    for a in 1..limit {
        for b in 1..limit {
            for c in 1..limit {
                if a + b + c == limit {
                    if pythagorean_theorem(a, b, c) {
                        println!("{} {} {}", a, b, c);
                        println!("{}", a * b * c);
                    }
                } 
            } 
        } 
    }
}
