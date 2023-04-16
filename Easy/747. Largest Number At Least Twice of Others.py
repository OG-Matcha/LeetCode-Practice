# easy

'''
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array 
is at least twice as much as every other number in the array. 
If it is, return the index of the largest element, or return -1 otherwise.
'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        maxi = max(nums)
        result = [i for i in nums]
        result.remove(maxi)
        
        for i in result:
            if i * 2 > maxi:
                return -1
            
        return nums.index(maxi)

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        temp = sorted(nums)
        
        if temp[-2] * 2 <= temp[-1]:
            return nums.index(max(nums))
        
        return -1