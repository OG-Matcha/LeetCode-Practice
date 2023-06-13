# medium

'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''

# https://leetcode.com/problems/equal-row-and-column-pairs/description/

import collections


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        data = collections.Counter(tuple(row) for row in grid)

        for i in range(len(grid)):
            col = tuple(grid[j][i] for j in range(len(grid)))
            count += data[col]

        return count

# Time complexity = O(n^2)
# Space complexity = O(n^2)
