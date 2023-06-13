# medium

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

# https://leetcode.com/problems/longest-consecutive-sequence/

# Hashset


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        maxi = 0

        for num in nums:
            if num - 1 not in data:
                length = 1
                while num + length in data:
                    length += 1
                maxi = max(maxi, length)

        return maxi

# Time complexity = O(n) where n is the length of nums
# Space complexity = O(n)
