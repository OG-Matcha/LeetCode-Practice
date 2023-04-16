# easy

'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        
        def ugly(n):
            if n == 0:
                return False
            if n == 1:
                return True
            if n % 2 == 0:
                return ugly(n // 2)
            elif n % 3 == 0:
                return ugly(n // 3)
            elif n % 5 == 0:
                return ugly(n // 5)
        return ugly(n)