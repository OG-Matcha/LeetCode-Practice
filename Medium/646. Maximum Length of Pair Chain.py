# medium

'''
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.
'''

# https://leetcode.com/problems/maximum-length-of-pair-chain/description/

# Greedy


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x: x[1])

        count = 1
        curr = pairs[0][1]

        for a, b in pairs:
            if curr < a:
                count += 1
                curr = b

        return count

# Time complexity = O(nlogn) where n is the length of pairs
# Space complexity = O(1)
