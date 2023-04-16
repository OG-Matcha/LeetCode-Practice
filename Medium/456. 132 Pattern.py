# medium

'''
Given an array of n integers nums,
a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        sec_num = -inf
        stack = []
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < sec_num:
                return True
            while stack and stack[-1] < nums[i]:
                sec_num = stack.pop()
            stack.append(nums[i])
        return False