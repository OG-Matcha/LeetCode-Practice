# medium

'''
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. 
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
'''

import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        
        res = 0
        data = collections.Counter(s)
        used = set()
        
        for char, freq in data.items():
            
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
                
            used.add(freq)
        
        return res

# Time complexity = O(N)
# Space complexity = O(1)