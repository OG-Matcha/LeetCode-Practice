# easy

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxi = 0
        smallest = prices[0]

        for price in prices:
            if price < smallest:
                smallest = price
            maxi = max(maxi, price - smallest)

        return maxi

# Time complexity = O(n) where n is the length of prices
# Space complexity = O(1)
