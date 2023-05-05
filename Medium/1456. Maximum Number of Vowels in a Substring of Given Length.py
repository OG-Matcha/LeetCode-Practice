# medium

'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# Sliding Window


class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"
        maxi = 0

        for i in range(k):
            if s[i] in vowels:
                maxi += 1

        temp = maxi

        for i in range(k, len(s)):
            if s[i] in vowels:
                temp += 1
            if s[i - k] in vowels:
                temp -= 1

            maxi = max(maxi, temp)

        return maxi


class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        end = k
        vowels = "aeiou"
        maxi = 0

        for i in range(k):
            if s[i] in vowels:
                maxi += 1

        temp = maxi

        while end < len(s):
            if s[end] in vowels:
                temp += 1
            if s[end - k] in vowels:
                temp -= 1

            maxi = max(maxi, temp)
            end += 1

        return maxi

# Time complexity = O(n) where n is the length of the word
# Space complexity = O(1)
