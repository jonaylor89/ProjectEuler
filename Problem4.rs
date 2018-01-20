
fn is_palindrome(question: i32) -> bool {
    let mut reverse_num = 0;
    let mut input = question;

    while input != 0 {
        reverse_num = reverse_num * 10 + input % 10;
        input = input / 10;
    }

    return question == reverse_num;
}

fn main() {
    let mut max: i32 = 0;
    let mut sum;

    for i in 100..999 {
        for j in 100..999 {
            sum = i * j;
            if is_palindrome(sum) && sum > max {
                max = sum; 
            }
        } 
    }

    println!("Sum: {}", max)
}
