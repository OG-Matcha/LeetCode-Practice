# easy

'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.
'''

# https://leetcode.com/problems/circular-sentence/description/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        data = sentence.split()
        
        for i in range(len(data)):
            if data[i - 1][-1] != data[i][0]:
                return False
        
        return True

# Time complexity = O(n)
# Space complexity = O(n)

class Solution:
    def isCircularSentence(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == " " and s[i-1] != s[i+1]:
                return False
        return s[0] == s[-1]

# Time complexity = O(n)
# Space complexity = O(1)