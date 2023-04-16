# medium

'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''

# https://leetcode.com/problems/longest-common-subsequence/description/

# Tabulation & Space optimized
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        len1 = len(text1)
        len2 = len(text2)
        
        prev = [0 for i in range(len2 + 1)]
        curr = [0 for i in range(len2 + 1)]
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if(text1[i - 1] == text2[j - 1]):
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = [i for i in curr]

        return prev[len2]

# Time complexity = O(m * n)
# Space complexity = O(min(m, n))