# easy

'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, 
such as pow(x, 0.5) or x ** 0.5.
'''

# Brute force
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: 
            return x
        s = 1
        while True:
            if s * s > x: 
                return s - 1
            s += 1

# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

# Newton’s method
class Solution:
    def mySqrt(self, x: int) -> int:
        num = x
        while num * num > x:
            num = (num + x // num) // 2
        return num