#RunTime: 40 ms
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2, -1, -1):
            for e in range(len(triangle[i])-1, -1, -1):
                a = triangle[i+1][e + 1]
                b = triangle[i+1][e]
                triangle[i][e] = triangle[i][e] + min(a, b)
        return triangle[0][0]
