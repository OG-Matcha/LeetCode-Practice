# easy

'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
'''

# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

# Brute-force with set
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        flag = 1
        count = 0
        length = len(s)
        vowels = set("aeiouAEIOU")

        for c in range(length):
            if c == length // 2:
                flag = 0
            if flag:
                 if s[c] in vowels:
                     count += 1
            if not flag:
                if s[c] in vowels:
                    count -= 1
        
        return count == 0

class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        count = 0
        half = len(s) // 2
        vowels = set("aeiouAEIOU")

        for i, c in enumerate(s):
            if c in vowels:
                count += 1 if i < half else -1 

        return count == 0

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half = len(s) // 2
        left = s[:half]
        right = s[half:]
        vowels = set("aeiouAEIOU")
        
        count_l = sum(1 for c in left if c in vowels)
        count_r = sum(1 for c in right if c in vowels)

        return count_l == count_r

# Time complexity = O(n)
# Space complexity = O(10)