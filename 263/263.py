#RunTime: 48 ms
class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num in [1, 2, 3, 5]:
            return True
        elif num == 0:
            return False
        else:
            for i in [2, 3, 5]:
                if num % i == 0:
                    return self.isUgly(num / i)
            return False
