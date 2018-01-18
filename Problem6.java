
class Problem6 {
    public static void main(String[] argv) {
        int limit = 100;

        int sum_of_squares = 0;
        int square_of_sum = 0;

        for(int i = 0; i <= limit; i++) {
            sum_of_squares += i * i; 
        }

        for(int j = 0; j <= limit; j++) {
            square_of_sum += j; 
        }

        square_of_sum *= square_of_sum;

        System.out.println(square_of_sum - sum_of_squares);

    }
}
