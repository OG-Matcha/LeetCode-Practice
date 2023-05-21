# medium

'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
'''

# https://leetcode.com/problems/shortest-bridge/description/

# Dfs & Bfs


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)

        def first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        return i, j

        def dfs(x, y):
            grid[x][y] = -1
            q.append((x, y))
            for cur_x, cur_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                    dfs(cur_x, cur_y)

        q = []
        dis = 0
        dfs(*first())

        while q:
            new_q = []
            for x, y in q:
                for cur_x, cur_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return dis
                        elif not grid[cur_x][cur_y]:
                            new_q.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1

            q = new_q
            dis += 1

# Time complexity: O(n^2) where n^2 is the size of the grid
# Space complexity: O(n^2)
