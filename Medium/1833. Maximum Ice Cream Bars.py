# medium

'''
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.

 
'''

# https://leetcode.com/problems/maximum-ice-cream-bars/description/

# Sort


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, v in enumerate(costs):
            coins -= v
            if coins < 0:
                return i

        return len(costs)


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for i in costs:
            if coins <= 0:
                break
            if coins >= i:
                res += 1
                coins -= i

        return res

# Time complexity = O(nlogn)
# Space complexity = O(1)
