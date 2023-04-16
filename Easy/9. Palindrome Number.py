# easy

'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = []
        if x < 0:
            return False
        while x > 0:
            arr.append(x - (x // 10) * 10)
            x = x//10
        return arr == arr[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reverse = 0
        orginal = x
        
        while x != 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return orginal == reverse