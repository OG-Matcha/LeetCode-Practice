# medium

'''
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
'''

# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

# Sorting & Two pointer


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()

        left = 0
        right = len(nums) - 1
        mod = 1000000007
        res = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                res += pow(2, right - left, mod)
                left += 1
            else:
                right -= 1

        return res % mod

# Time complexity = O(nlogn) where n is the length of nums
# Space complexity = O(1)
