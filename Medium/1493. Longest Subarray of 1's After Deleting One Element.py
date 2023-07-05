# medium

'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        count = 0

        for right in nums:

            if right == 0:
                count += 1

            if count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1

        return len(nums) - left - 1


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        start = 0
        count = 0
        maxi = 0

        for end, right in enumerate(nums):

            if right == 0:
                count += 1

            while count > 1:
                if nums[start] == 0:
                    count -= 1
                start += 1

            maxi = max(maxi, end - start)

        return maxi

# Time complexity = O(n) where n is the length of nums
# Time complexity = O(1)
