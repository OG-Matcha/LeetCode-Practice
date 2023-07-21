# medium

'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing. 
'''

# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        length = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        maxi = max(length)
        res = 0

        for i in range(len(nums)):
            if length[i] == maxi:
                res += count[i]

        return res

# Time complexity = O(n^2) where n is the length of nums
# Space complexity = O(n)
