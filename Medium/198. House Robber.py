# medium

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

# https://leetcode.com/problems/house-robber/description/

# Space optimized
class Solution:
    def rob(self, nums: List[int]) -> int:

        cur = prev = prev2 = 0

        for house in nums:
            cur = max(prev, house + prev2)
            prev2 = prev
            prev = cur
        
        return cur

# Time complexity = O(n)
# Space complexity = O(1)