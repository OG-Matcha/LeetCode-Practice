# medium
# https://leetcode.com/problems/longest-consecutive-sequence/

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

# Hashset
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0
        
        for i in nums_set:
            if i - 1 not in nums_set:
                curr_num = i
                streak = 1
                
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    streak += 1
                
                longest = max(longest, streak)
        
        return longest

# Time complexity = O(N)
# Space complexity = O(N)