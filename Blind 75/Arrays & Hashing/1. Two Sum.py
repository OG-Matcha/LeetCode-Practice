# easy

'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value

            if remaining in seen:
                return [seen[remaining], i]

            seen[value] = i

# Time complexity = O(n) where n is the length of the nums arraya
# Space complexity = O(n)
