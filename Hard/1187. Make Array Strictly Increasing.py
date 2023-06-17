# hard

'''
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.
'''

# https://leetcode.com/problems/make-array-strictly-increasing/description/

''' Logical Thinking
Record the possible states of each position and number of operations to get this state.
When we check i-th element in the arr1, dp record the possible values we can place at this position, and the number of operations to get to this state.
Now, we need to build dp for (i+1)-th position, so for (i+1)-th element,
if it's larger than the possible state from i-th state, we have two choices:
1. keep it so no operation needs to be made.
2. choose from arr2 a smaller element that is larger than i-th element and add one operation.
If it's not larger than the i-th state, we definitely need to make a possible operation.
'''




import collections
import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        dp = {-1: 0}
        arr2.sort()

        for i in range(len(arr1)):
            new_dp = collections.defaultdict(lambda: float("inf"))

            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])

                idx = bisect.bisect_right(arr2, prev)

                if idx < len(arr2):
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], dp[prev] + 1)

            dp = new_dp

        return min(dp.values()) if dp else -1

# Time complexity = O(m * nlogn) where m is the length of arr1 and n is the length of arr2
# Space complexity = O(m)
