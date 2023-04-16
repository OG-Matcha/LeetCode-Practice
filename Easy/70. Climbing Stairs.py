# easy

'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

# https://leetcode.com/problems/climbing-stairs/description/

# Dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n

        res = [0] * n
        res[0], res[1] = 1, 2

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]

        return res[n - 1]

class Solution:
    def climbStairs(self, n: int) -> int:

        res = [1, 2, 3] + [0] * n

        for i in range(3, n):
            res[i] = res[i - 1] + res[i - 1] - res[i - 3]

        return res[n - 1]

# Time complexity = O(n)
# Space complexity = O(n)

# Optimized
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        curr = prev = 1

        for i in range(1, n):
            curr, prev = curr + prev, curr
        
        return curr

# Time complexity = O(n)
# Space complexity = O(1)