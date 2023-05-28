# hard

'''
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.
'''

# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts + [0, n])
        k = len(cuts)
        dp = [[0] * k for _ in range(k)]

        for d in range(2, k):
            for i in range(k - d):
                dp[i][i+d] = min(dp[i][m] + dp[m][i+d]
                                 for m in range(i+1, i+d)) + cuts[i+d] - cuts[i]

        return dp[0][k-1]

# Time complexity = O(k^3)
# Space complexity = O(k^2)
