# easy

'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Two pointer
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        head = 0
        rear = len(s)-1
        data = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        while head < rear:

            while head < len(s) and s[head] not in data:
                head += 1
            while rear > 0 and s[rear] not in data:
                rear -= 1

            if head < rear:
                s[head], s[rear] = s[rear], s[head]
                head += 1
                rear -= 1
        
        return "".join(s)

# Time complexity = O(n)
# Space complexity = O(n)