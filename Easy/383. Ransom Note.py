# easy

'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

# https://leetcode.com/problems/ransom-note/

# Hash table(set)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        
        return True

# Find & Replace
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for letter in ransomNote:
            if magazine.find(letter) != -1:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False
            
        return True