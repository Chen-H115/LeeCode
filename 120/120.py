class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2, -1, -1):
            for idx in range(len(triangle[i])-1, -1, -1):
                a = triangle[i+1][idx + 1]
                b = triangle[i+1][idx]
                triangle[i][idx] = triangle[i][idx] + min(a, b)
        return triangle[0][0]
