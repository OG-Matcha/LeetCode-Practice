# easy

'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num = 0
        result = []
        
        for i in range(len(nums)):
            num += nums[i]
            result.append(num)
            
        return result

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i + 1]) for i in range(len(nums))]


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums