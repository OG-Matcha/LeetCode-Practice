# medium

'''
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.
'''

# https://leetcode.com/problems/uncrossed-lines/description/

# Dynamic Programming


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        dp = [0] * n
        res = 0

        for num in nums2:
            cnt = 0
            for i in range(n):
                if cnt < dp[i]:
                    cnt = dp[i]
                elif num == nums1[i]:
                    dp[i] = cnt + 1
                    res = max(res, dp[i])
        return res

# Time complexity = O(n * m) where n and m are the length of given input
# Space complexity = O(min(n, m))
