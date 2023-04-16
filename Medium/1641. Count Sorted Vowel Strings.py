# medium

'''
Given an integer n, 
return the number of strings of length n that consist only of vowels (a, e, i, o, u) 
and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, 
s[i] is the same as or comes before s[i+1] in the alphabet.
'''

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(list(combinations_with_replacement(["a","e","i","o","u"], n)))

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24