# medium

'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        length = len(triangle)
        
        for r in range(1, length):
            
            n = len(triangle[r])
            
            for i in range(n):
                
                if i == 0:
                    triangle[r][i] += triangle[r - 1][i]
                elif i == n - 1:
                    triangle[r][i] += triangle[r - 1][i - 1]
                else:
                    mini = min(triangle[r - 1][i], triangle[r - 1][i - 1])
                    triangle[r][i] += mini
        
        return min(triangle[length - 1])

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle: 
            return
        
        row = triangle[-1]

        for i in range(len(triangle)-2, -1,-1):
            for j in range(len(triangle[i])):
                row[j] = min(row[j], row[j + 1]) + triangle[i][j]

        return row[0]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = [0] * (len(triangle) + 1)
        
        for row in triangle[::-1]:
            
            for i, n in enumerate(row):
                
                dp[i] = n + min(dp[i], dp[i + 1])
        
        return dp[0]
        
# Time - O(N^2) - where N is the number of values
# Space - O(N) - the number of rows