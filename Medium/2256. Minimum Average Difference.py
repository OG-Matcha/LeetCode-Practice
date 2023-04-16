# meduium

'''
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.
'''

# https://leetcode.com/problems/minimum-average-difference/description/

# Prefix & Surfix
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        length = len(nums)

        mini_idx = 0
        mini_avg = inf

        pre = 0
        suf = sum(nums)

        for idx, val in enumerate(nums, start=1):
            pre += val
            suf -= val

            right_count = length - idx or 1
            diff = abs(pre // idx - suf // right_count)

            if diff < mini_avg:
                mini_avg = diff
                mini_idx = idx - 1
        
        return mini_idx

# Time complexity = O(n)
# Space complexity = O(1)