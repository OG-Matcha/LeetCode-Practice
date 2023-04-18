# easy

'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

# https://leetcode.com/problems/merge-strings-alternately/description/


from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""
        length = min(len(word1), len(word2))

        for i in range(length):
            res += word1[i] + word2[i]

        return res + word1[length:] + word2[length:]

# Time complexity = O(m + n) where m and n are the length of words
# Time complexity = O(m + n)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))

# Time complexity = O(m + n) where m and n are the length of words
# Time complexity = O(m + n)
