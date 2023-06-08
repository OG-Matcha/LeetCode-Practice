# easy

'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
'''

# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

import bisect

# Binary Search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            count += len(row) - bisect.bisect_right(row, 0, key=lambda x: -x)

        return count

# Time complexity = O(mlogn) where m × n is the size of the input matrix
# Space complexity = O(1)


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count = 0
        n = len(grid[0])
        curr = n - 1

        for row in grid:
            while curr >= 0 and row[curr] < 0:
                curr -= 1

            count += n - curr - 1

        return count

# Time complexity = O(m + n)
# Space complexity = O(1)
