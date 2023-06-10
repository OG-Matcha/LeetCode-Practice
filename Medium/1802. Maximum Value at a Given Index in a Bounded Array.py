# medium

'''
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.
'''

# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/editorial/


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def check(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a

        maxSum -= n
        left = 0
        right = maxSum + 1

        while left < right:
            mid = left + (right - left) // 2
            if check(mid) <= maxSum:
                left = mid + 1
            else:
                right = mid

        return left

# Time complexity = O(log(maxSum))
# Space complexity = O(1)
