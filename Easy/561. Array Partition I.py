# easy

'''
Given an integer array nums of 2n integers, 
group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) 
for all i is maximized. Return the maximized sum.
'''

class Solution: # 0.532261
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([num for num in sorted(nums)[::2]])

class Solution: # 0.3547696
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

class Solution: # 0.2616824
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])