
class Problem4 {
    public static void main(String[] argv) {

        long max = 0;

        for(int i = 100; i < 999; i++) {
            for(int j = 100; j < 999; j++) {
                int sum = i * j;
                if(isPalindrome(sum) && sum > max) {
                    max = sum; 
                }
            }
        }

        System.out.println(max);

    }

    static boolean isPalindrome(int question) {
         int reverseNum = 0;
         int input = question;

         while(input != 0) {
            reverseNum = reverseNum * 10 + input % 10;
            input = input / 10;
         }

        return question == reverseNum;

    }
}


