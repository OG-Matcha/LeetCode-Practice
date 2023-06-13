# easy

'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = set()

        for num in nums:
            if num in data:
                return True
            data.add(num)

        return False


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

# Time complexity = O(n)
# Space complexity = O(1)
