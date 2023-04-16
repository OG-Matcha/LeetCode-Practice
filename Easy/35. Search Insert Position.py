# easy

'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for index, num in enumerate(nums):
                if num > target:
                    return index
            else:
                return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
                
            elif nums[mid] > target:
                right = mid - 1
                
            else:
                return mid
                
        return left if target <= nums[left] else left + 1