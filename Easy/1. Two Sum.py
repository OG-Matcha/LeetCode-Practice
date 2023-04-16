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

# Time complexity = O(n) as it iterates through the list of nums only once.
# Space complexity = O(n) where n is the length of the nums array.


""" 
This code is a solution to the Two Sum problem. It takes an array of numbers (nums) and a target number as input and returns two indices from the array that sum up to the target. The code uses a dictionary (seen) to store each number from the array and its index. It then iterates through the array and checks if the difference between the target and current value is in the dictionary. If it is, then it returns an array containing both indices. If not, it adds the current value and its index to the dictionary. 
"""
