# hard

'''
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.
'''

# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/

''' Logical Thinking
The solve method takes the current grid, cell coordinates, the previous value (for comparison), and the memoization array dp. It first checks the base cases: if the current cell is out of bounds or has a value less than or equal to the previous value, it returns 0. If the result for the current cell is already calculated and stored in dp, it directly returns the stored value.

If the base cases are not met, the method recursively calls itself for the left, right, up, and down neighboring cells. It passes the current cell value as the new previous value to ensure that paths only move to cells with greater values. The results from these recursive calls are summed up, and 1 is added to account for the current cell. The sum is then stored in dp for memoization.
'''


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        mod = 1000000007
        dire = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):

            if dp[i][j]:
                return dp[i][j]

            ans = 1

            for di, dj in dire:
                prev_i = i + di
                prev_j = j + dj

                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    ans += dfs(prev_i, prev_j) % mod

            dp[i][j] = ans
            return ans

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod

# Time complexity = O(m * n) where m * n is the size of grid
# Space complexity = O(m * n)
