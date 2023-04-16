# easy

'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for i in nums:
            count = 0
            while i >= 10:
                i //= 10
                count += 1
            if count == 0:
                continue
            if count % 2 != 0:
                even += 1
        return even