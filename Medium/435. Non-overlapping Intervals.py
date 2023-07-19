# medium

'''
Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

# https://leetcode.com/problems/non-overlapping-intervals/description/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        res = 0
        k = -float('inf')

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                res += 1

        return res

# Time complexity = O(nlogn) where n is the length of intervals
# Time complexity = O(n)
