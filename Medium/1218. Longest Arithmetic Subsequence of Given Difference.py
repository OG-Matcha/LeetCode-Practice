# medium

'''
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
'''

# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/submissions/


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = dict()
        res = 1

        for i in arr:
            last = dp.get(i - difference, 0)
            dp[i] = last + 1
            res = max(res, dp[i])

        return res

# Time complexity = O(n) where n is the length of arr
# Space complexity = O(n)
