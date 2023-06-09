# easy

'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
'''

# https://leetcode.com/problems/largest-perimeter-triangle/

# Sort
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        
        for i in range(len(nums)-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

# Time complexity = O(n)
# Space complexity = O(1)