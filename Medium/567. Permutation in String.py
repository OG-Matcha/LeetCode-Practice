# medium

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''

# https://leetcode.com/problems/permutation-in-string/description/

# Sliding Windows


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        words1 = collections.Counter(s1)
        words2 = collections.Counter(s2[:len(s1)])

        if words1 == words2:
            return True

        for i in range(len(s2) - len(s1)):
            if words1 == words2:
                return True
            words2[s2[i]] -= 1
            words2[s2[i+len(s1)]] += 1
            if words1 == words2:
                return True

        return False

# Time complexity = O(n)
# Space complexity = O(1)
