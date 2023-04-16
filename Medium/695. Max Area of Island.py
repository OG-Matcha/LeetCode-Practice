# medium

'''
You are given an m x n binary matrix grid. 
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

# Dfs recursion
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans, n, m = 0, len(grid), len(grid[0])
        
        def trav(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            
            return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
        
        for i, j in product(range(n), range(m)):
            if grid[i][j]: 
                ans = max(ans, trav(i, j))
                
        return ans

# Time complexity = O(n * m)
# Space complexity = O(l)