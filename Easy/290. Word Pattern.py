# easy

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

# https://leetcode.com/problems/word-pattern/description/

# Hash Table
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        data = dict()
        words = s.split()

        if len(set(pattern)) != len(set(words)) or len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in data and data[pattern[i]] != words[i]:
                return False
            else:
                data[pattern[i]] = words[i]

        return True


# Time complexity = O(n)
# Space complexity = O(n)

# Itertools
import itertools


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        return (
            len(set(pattern))
            == len(set(words))
            == len(set(itertools.zip_longest(pattern, s)))
        )


# Time complexity = O(n)
# Space complexity = O(n)
