#Runtime: 44 ms
class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        check = []
        def helper(x):
            sum = 0
            for i in str(x):
                sum = sum + int(i) ** 2
            if sum in check:
                return False
            if sum == 1:
                return True
            else:
                check.append(sum)
                return helper(sum)
        return helper(n)
