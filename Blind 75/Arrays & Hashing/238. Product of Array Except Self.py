# medium

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]

        pos = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pos
            pos *= nums[i]

        return res

# Time complexity = O(n) where n is the length of nums
# Space complexity = O(n)
