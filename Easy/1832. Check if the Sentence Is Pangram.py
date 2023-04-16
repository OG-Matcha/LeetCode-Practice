# easy

'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
'''

# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# Hash table
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        return len(set(i for i in sentence)) == 26

# Time complexity = O(n)
# Space complexity = O(1)