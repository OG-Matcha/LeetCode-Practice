# medium

'''
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        window_start = 0
        min_len = inf
        curr_sum = 0
        
        for window_end in range(len(nums)):
            curr_sum += nums[window_end]
            
            while(curr_sum >= target):
                min_len = min(min_len, window_end - window_start + 1)
                curr_sum -= nums[window_start]
                window_start += 1
                
        if min_len == math.inf:
            return 0
            
        return min_len
		