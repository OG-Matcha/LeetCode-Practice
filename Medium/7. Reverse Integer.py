# medium

'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        if x > 0:
            result = int(str(x)[::-1])
            return 0 if result > 2 ** 31 - 1 else result
        
        if x < 0:
            result = int(str(abs(x))[::-1]) * -1
            return 0 if result < -2 ** 31 else result

class Solution:
    def reverse(self, x: int) -> int:
        
        if not x:
            return 0
        
        is_positive = 1 if x > 0 else -1
        
        x = abs(x)
        
        while not x % 10:
            x //= 10
            
        value = is_positive * int(str(x)[::-1])
        
        if value < -2 ** 31 or value > 2 ** 31 - 1:
            return 0
        
        return value
        
            