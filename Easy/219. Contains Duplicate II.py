# easy

'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

# https://leetcode.com/problems/contains-duplicate-ii/

# Dictionary
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        data = dict()
        
        for i, num in enumerate(nums):
            if num in data and i - data[num] <= k:
                return True
            data[num] = i
        
        return False

# Set & Sliding window
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        curr = set()
        
        for i, num in enumerate(nums):
            
            if num in curr:
                return True
            
            curr.add(num)
            
            if len(curr) > k:
                curr.remove(nums[i-k])