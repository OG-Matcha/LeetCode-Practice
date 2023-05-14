# hard

'''
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.
'''

# https://leetcode.com/problems/maximize-score-after-n-operations/description/

# Bit Mask & Dfs


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, mask):

            if i > len(nums) // 2:
                return 0

            res = 0

            for j in range(len(nums)):

                if (mask >> j) & 1:
                    continue

                for k in range(j + 1, len(nums)):

                    if (mask >> k) & 1:
                        continue

                    new_mask = (1 << j) | (1 << k) | mask
                    res = max(
                        res, i * gcd(nums[j], nums[k]) + dfs(i + 1, new_mask))

            return res

        return dfs(1, 0)

# Time complexity = O(2^n * n^2) where n is the length of nums
# Space complexity = O(2^n)
