# easy

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            if temp > max:
                max = temp
            if i == 0:
                temp = 0
        return max