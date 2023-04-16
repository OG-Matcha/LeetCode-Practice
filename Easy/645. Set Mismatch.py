# easy

'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''

# https://leetcode.com/problems/set-mismatch/

# Hashmap
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        hashmap = dict()
        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            
        for i in range(1, len(nums) + 1):
            if i in hashmap:
                if hashmap[i] == 2:
                    dup = i
            else:
                missing = i
        
        return [dup, missing]

# Time complexity = O(n) Traversing over nums of size n takes O(n) time.
# Space complexity = O(n) Map can contain atmost n entries for each of the numbers from 1 to n.

# formula
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        range_sum = n * (n + 1) // 2
        real_sum = sum(nums)
        set_sum = sum(set(nums))
        
        return [real_sum - set_sum, range_sum - set_sum]

# Time complexity = O(n)
# Space complexity = O(1)