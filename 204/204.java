class Solution {
    public static boolean isPrime(int n){
            if (n <= 3)
                 return n > 1;
            else{
                for(int i=2;i<=Math.sqrt(n);i++){
                    if(n%i == 0)
                        return false;
                }
            }
            return true;
          }
    public int countPrimes(int n) {
        n -= 1;
        int sum = 0;
        for (int i = 1; i <= n; i++){
             if (isPrime(i)) {
                sum++;
             }
        }
        return sum;
    }
}
