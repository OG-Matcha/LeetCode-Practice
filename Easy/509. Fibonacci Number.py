# easy
# https://leetcode.com/problems/fibonacci-number/

'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. 
That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
'''

# Recursive


class Solution:
    def fib(self, n: int) -> int:

        def helper(n):

            if n == 0:
                return 0

            elif n == 1 or n == 2:
                return 1

            else:
                return helper(n - 1) + helper(n - 2)

        return helper(n)

# Dynamic programming


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a = 0
        b = 1
        c = a + b

        for _ in range(n - 1):
            b = c
            a = b
            c = a + b

        return c
