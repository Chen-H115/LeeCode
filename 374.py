#S1 Runtime: 20 ms
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1;
        high = n;
        while low <= high:
            mid = low + (high - low) / 2;
            res = guess(mid);
            if res == 0:
                return mid;
            elif res < 0:
                high = mid - 1;
            else:
                low = mid + 1;
#S2 Runtime: 16 ms
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1;
        high = n;
        while True:
            mid1 = low + (high - low) // 3;
            mid2 = high - (high - low) // 3;
            if guess(mid1) == 0:
                return mid1;
            if guess(mid2) == 0:
                return mid2;
            elif guess(mid1) < 0:
                high = mid1 - 1
            elif guess(mid2) > 0:
                low = mid2 + 1
            else:
                    low = mid1 + 1
                    high = mid2 - 1
#S2 Runtime: 20 ms
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1;
        high = n;
        while True:
            mid1 = low + (high - low) // 4;
            mid2 = (high + low) // 2;
            mid3 = high - (high - low) // 4;
            if guess(mid1) == 0:
                return mid1;
            if guess(mid2) == 0:
                return mid2;
            if guess(mid3) == 0:
                return mid3;
            elif guess(mid1) < 0:
                high = mid1 - 1
            elif guess(mid3) > 0:
                low = mid3 + 1
            else:
                if guess(mid2) < 0:
                    low = mid1 + 1
                    high = mid2 - 1
                else:
                    low = mid2 + 1
                    high = mid3 - 1
