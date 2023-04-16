# medium

'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
'''

# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
    
        s = '1'
        
        for _ in range(n-1):
            
            first = s[0]
            res = ""
            count = 0
            
            for i in s:
                if i == first:
                    count += 1
                else:
                    res += str(count) + first
                    first = i
                    count = 1
            res += str(count) + first
            s = res
            
        return s