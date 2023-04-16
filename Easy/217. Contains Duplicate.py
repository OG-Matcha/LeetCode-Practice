# easy

'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hash = set()
        length = 0
        
        for i in nums:
            hash.add(i)
            length += 1
            
            if len(hash) != length:
                return True
            
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums) 