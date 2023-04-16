# medium
# https://leetcode.com/problems/wiggle-subsequence/

'''
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between 
positive and negative. The first difference (if one exists) may be either positive or negative. 
A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

• For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) 
  alternate between positive and negative.
• In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. 
  The first is not because its first two differences are positive, 
  and the second is not because its last difference is zero.

A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
'''

# Greedy
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        check = None
        length = 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0 and check != True:
                length += 1
                check = True
            if nums[i] - nums[i-1] < 0 and check != False:
                length += 1
                check = False
        
        return length

# Time complexity = O(N)
# Space complexity = O(1)

# Dynamic programming (Space-Optimized)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return len(nums)
        
        up = down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        
        return max(up, down)

# Time complexity = O(N)
# Space complexity = O(1)

# Brute-force (TLE)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        def calculate(nums, index, up):
            maxcount = 0
            for i in range(index+1, len(nums)):
                if (up and nums[i] > nums[index]) or (not up and nums[i] < nums[index]):
                    maxcount = max(maxcount, 1 + calculate(nums, i, not up))
            
            return maxcount
        
        if len(nums) < 2:
            return len(nums)
        
        return 1 + max(calculate(nums, 0, True), calculate(nums, 0, False))

# Time complexity = O(N!)
# Space complexity = O(N)