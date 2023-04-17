# easy

'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

# Greedy


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        for i, v in enumerate(candies):
            candies[i] = v + extraCandies >= maxi

        return candies

# Time complexity = O(n) where n is the number of kids
# Space complexity = O(1)
