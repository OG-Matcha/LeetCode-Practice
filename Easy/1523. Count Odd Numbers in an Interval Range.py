# easy

'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''

# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high % 2 or low % 2)

# Time complexity = O(1)
# Space complexity = O(1)