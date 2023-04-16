# medium

'''
Given an array nums with n integers, 
your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds 
for every i (0-based) such that (0 <= i <= n - 2).
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        check = False
        
        for i in range(1, len(nums)):

            if nums[i] < nums[i-1]:

                if check or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False

                check = True

        return True

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        change = False
        
        for i in range(len(nums) - 1):
            
            if nums[i] <= nums[i+1]:
                continue
            if change:
                return False
            
            if i == 0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
                
            change = True
        
        return True

# Time complexity = O(N)
# Space ccomplexity = O(1)