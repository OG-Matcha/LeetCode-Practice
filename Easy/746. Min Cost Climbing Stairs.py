# easy
# https://leetcode.com/problems/min-cost-climbing-stairs/

'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

# Dynamic programming
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if not cost:
            return 0

        dp = [0] * len(cost)
        dp[0] = cost[0]

        if len(cost) >= 2:
            dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])

# Time complexity = O(n)
# Space complexity = O(n)

