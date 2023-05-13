# medium

'''
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
'''

# https://leetcode.com/problems/count-ways-to-build-good-strings/description/

# Dynamic Programming


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [1] + [0] * high
        mod = 1000000007

        for end in range(1, high + 1):
            dp[end] = (dp[end - zero] + dp[end - one]) % mod

        return sum(dp[low:]) % mod

# Time complexity = O(high)
# Space complexity = O(high)
