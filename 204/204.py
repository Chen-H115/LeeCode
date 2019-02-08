#Low Memory
#Runtime: 11216 ms
class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        def isPrime(n):
            if n <= 3:
                 return n > 1
            else:
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n%i == 0:
                        return False
            return True
        sum = 0
        for i in range(1, n):
            if isPrime(i):
                sum += 1
        return sum
