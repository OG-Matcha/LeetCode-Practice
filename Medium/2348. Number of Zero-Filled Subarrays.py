# medium

'''
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        count = 0
        ans = 0

        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            ans += count

        return ans

# Time complexity = O(n) where n is the length of the given nums
# Space complexity = O(1)
