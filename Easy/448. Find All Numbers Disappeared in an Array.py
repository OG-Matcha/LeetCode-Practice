# easy

'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        hash_map = {i : False for i in range(1, len(nums) + 1)}
        
        for i in nums:
            hash_map[i] = True
            
        result = [key for key, value in hash_map.items() if not value]
        
        return result
            

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = []
        length = len(nums)
        nums = set(nums)
        
        for i in range(1, length + 1):
            if i not in nums:
                result.append(i)
                
        return result