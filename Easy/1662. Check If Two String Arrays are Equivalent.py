# easy

'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''

# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

# Time complexity = O(n) where n is the length of the longer string
# Space complexity = O(n)

# Generator
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        def char(words):
            for word in words:
                for c in word:
                    yield c
            yield None
        
        return all(c1 == c2 for c1, c2 in zip(char(word1), char(word2)))

# Time complexity = O(min(m, n)) exits when it finds the first mismatch character
# Space comeplexity = O(1) we doesn't store any inputs and makes comparison one char at a time on the fly.