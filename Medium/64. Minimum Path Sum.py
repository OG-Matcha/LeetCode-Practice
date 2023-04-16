# medium

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

# https://leetcode.com/problems/minimum-path-sum/description/

# Dynamic Programming


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        for i in range(1, row):
            grid[i][0] += grid[i-1][0]

        for i in range(1, col):
            grid[0][i] += grid[0][i-1]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[row - 1][col - 1]

# Time complexity = O(m * n) where m and n are the dimensions of the input grid
# Space complexity = O(1)
