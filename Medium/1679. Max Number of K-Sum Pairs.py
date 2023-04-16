# medium

'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left, right = 0, len(nums) - 1
        answer = 0
        
        while left < right:
            if nums[left] + nums[right] == k:
                answer += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return answer