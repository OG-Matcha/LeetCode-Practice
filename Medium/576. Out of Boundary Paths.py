# medium

'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent cells in the grid 
(possibly out of the grid crossing the grid boundary). 
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, 
return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 10 ^ 9 + 7.
'''

# Breute-force (TLE)
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
            return 1
        if maxMove == 0:
            return 0
        
        return (self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) + self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn) + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)) % 1000000007

# Time complexity = O(4 ^ n)
# Space complexity = O(n)

# Recursion
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def moves(move,row,col):
            if row == m or row < 0 or col < 0 or col == n:
                return 1
            if move == 0:
                return 0
            move -= 1
            
            return (moves(move, row + 1, col) + moves(move, row, col + 1) + moves(move, row - 1, col) + moves(move, row, col - 1)) % ((10 ** 9) + 7)
        
        
        return moves(maxMove, startRow, startColumn)

# Dynamic programming
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        if maxMove == 0:
            return 0
        
        dpCurr = [[0] * (n+2) for _ in range(m+2)]
        dpLast = [[0] * (n+2) for _ in range(m+2)]
        
        for i in range(1, m+1):
            dpCurr[i][1] += 1
            dpCurr[i][n] += 1
            
        for j in range(1, n+1):
            dpCurr[1][j] += 1
            dpCurr[m][j] += 1
            
        ans = dpCurr[startRow+1][startColumn+1]
        
        for d in range(maxMove-1):
            dpCurr, dpLast = dpLast, dpCurr
            
            for i, j in product(range(1, m+1), range(1, n+1)):
                dpCurr[i][j] = (dpLast[i-1][j] + dpLast[i+1][j] + dpLast[i][j-1] + dpLast[i][j+1]) % 1000000007
                
            ans = (ans + dpCurr[startRow+1][startColumn+1]) % 1000000007
            
        return ans

# Time complexity = O(m * n * N)
# Space complexity = O(m * n)