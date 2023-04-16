# easy

'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashMap = {}
        mx = 0
        res = 0
        
        for n in nums :
            
            if n not in hashMap :
                hashMap[n] = 1
                
            else :
                hashMap[n] += 1
                
            if hashMap[n] > mx :
                mx = hashMap[n]
                res = n
                
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res, count = nums[0], 0
		
        for n in nums :
            
            if res == n :
                count += 1
            else : 
                if count == 0:
                    res = n
                else :
                    count -= 1
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        return nums[len(nums) // 2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mid = len(nums) / 2
        hash = {}
        
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
            
            if hash[i] >= mid:
                return i