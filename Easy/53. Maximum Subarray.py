# easy

'''
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''
# from cmath import inf

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = sum = -inf
        
        for i in nums:
            sum = max(i,sum + i)
            maxSum = max(sum,maxSum)
        return maxSum