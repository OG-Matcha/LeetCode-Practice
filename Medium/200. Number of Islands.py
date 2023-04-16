# medium

'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = set()
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j, nums, island):
            if (i, j) in island or i < 0 or i > row - 1 or j < 0 or j > col - 1 or grid[i][j] == "0":
                return nums
            
            island.add((i, j))
            dfs(i - 1, j, nums, island)
            dfs(i + 1, j, nums, island)
            dfs(i, j - 1, nums, island)
            dfs(i, j + 1, nums, island)
            
            return nums + 1
        
        count = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count = dfs(i, j, count, islands)
        
        return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        islands=0
        
        def visit(r,c):
            
            grid[r][c]="2"
            
            if r < row - 1: 
                if grid[r + 1][c] == "1": 
                    visit(r + 1, c)
            if r > 0: 
                if grid[r - 1][c] == "1": 
                    visit(r - 1, c)
            if c < col - 1:
                if grid[r][c + 1] == "1": 
                    visit(r, c + 1)
            if c > 0: 
                if grid[r][c - 1] == "1": 
                    visit(r, c - 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1": 
                    islands += 1
                    visit(i, j)
                    
        return islands