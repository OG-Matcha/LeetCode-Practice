# medium

'''
Given a collection of numbers, nums, 
that might contain duplicates, return all possible unique permutations in any order.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        stack = []
        for i in list(permutations(nums, len(nums))):
            if i not in stack:
                stack.append(i)
        return stack

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))