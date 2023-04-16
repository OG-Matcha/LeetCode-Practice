# easy

'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            ans = 0
            while num > 0:
                rem = (num % 10)
                ans += rem
                num //= 10
            num = ans
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

