# easy

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

# https://leetcode.com/problems/valid-anagram/description/

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = collections.defaultdict(int)
        count_t = collections.defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1

        return count_s == count_t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

# Time complexity = O(n) where n is the length of the input
# Space complexity = O(n) or O(1) if we consider the hash map at most contains only 26 letters


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False

# Time complexity = O(nlogn)
# Space complexity = O(n)
