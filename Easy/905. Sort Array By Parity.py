# easy

'''
Given an integer array nums, 
move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        numbers = []
        for i in nums:
            if i % 2 != 0:
                numbers.append(i)
            else:
                numbers.insert(0, i)
        return numbers
                
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [i for i in nums if (i % 2) == 0] + [i for i in nums if (i % 2) != 0]