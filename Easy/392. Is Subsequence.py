# easy

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)
        if not(stack):
            return not(stack)
        for i in t:
            if not(stack):
                break
            if stack[0] == i:
                stack.pop(0)
        return not(stack)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lstT = iter(t)
        for i in s:
            if i not in lstT:
                return False
        return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for i in s:
            if not (i in t[idx:]):
                return False
            idx += t[idx:].index(i) + 1
        return True