# easy

'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

# https://leetcode.com/problems/n-th-tribonacci-number/description/


class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1

        if n == 0:
            return 0

        for _ in range(n - 2):
            now = first + second + third
            first = second
            second = third
            third = now

        return third

# Time complexity = O(n)
# Space complexity = O(n)
