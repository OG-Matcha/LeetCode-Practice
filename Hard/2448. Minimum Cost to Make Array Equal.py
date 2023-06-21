# hard

'''
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.
'''

# https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/

''' Logical Thinking
This approach is based on one theorem: a linear combination (with non-negative coefficients) of convex functions is convex.

Therefore, we can use binary search to locate the minimum of this convex function. Start with setting the boundaries of the search space as left = min(nums) and right = max(nums), we cut the search space into two halves by mid = (left + right) / 2. Then we shall determine which part contains the minimum cost. This can be done by comparing the cost of two adjacent bases:

If F(x) < F(x+1), it means the base that brings the minimum cost is on F(x)'s left, thus we should cut the right half.
If F(x) >= F(x+1), it means the base that brings the minimum cost is on F(x)'s right, thus we should cut the left half.

We continue the binary search until we reach the base that brings the minimum cost.
'''


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def total(curr):
            return sum(abs(curr - num) * c for num, c in zip(nums, cost))

        left = min(nums)
        right = max(nums)
        res = total(nums[0])

        while left < right:
            mid = left + (right - left) // 2
            first = total(mid)
            second = total(mid + 1)
            res = min(first, second)

            if first > second:
                left = mid + 1
            else:
                right = mid

        return res

# Time complexity = O(nlogk) where n is the length of nums and k is the difference between the maximum and minimum value of nums[i].
# Space complexity = O(1)


''' Logical Thinking
We find the weighted median of nums by sorting the (num, weight) pair of the original arrays. We then use the weighted median (target) to calculate the minimum total cost such that all the elements of the array nums becomes equal, which is the answer to this question.
'''


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        mid = sum(cost) / 2
        count = 0
        for target, co in arr:
            count += co
            if count >= mid:
                return sum(abs(target - num) * c for num, c in arr)

# Time complexity = O(nlogn)
# Space complexity = O(n)
