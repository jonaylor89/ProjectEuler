

import java.util.ArrayList;

class Problem3 {

    static ArrayList<Long> factors = new ArrayList<Long>();

    public static void main(String[] argv) {

        long n = 600851475143L;

        factorize(n);

        System.out.println(factors.get(factors.size() - 1));
    } 
    

    static boolean isPrime(long p) {
        if(p == 3 || p == 2 || p == 1) {
            return true; 
        }

        if(p % 2 == 0) {
            return false;
        }

        double sqrt_p = Math.sqrt(p);

        for(int i = 3; i < ((int) sqrt_p) + 1; i += 2) {
            if(p % i == 0) {
                return false; 
            }
        }

        return true;
    }

    static void factorize(long n) {
        if(isPrime(n)){
            factors.add(n);
        }else {
            for(int i = 2; i < n; i++) {
                if(n % i == 0) {
                    factorize(n / i);
                    factorize(i);
                }
            }
        }
    }
}

