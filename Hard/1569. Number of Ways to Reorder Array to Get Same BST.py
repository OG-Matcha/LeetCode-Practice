# hard

'''
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.
'''

# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/

''' Logical Thinking
We separate all the elements into two lists, depending on whether they are less than or more than the root. Then we recurse on those left and right sublists. The combination is for the macro ordering between left and right, and the recursive factors are for the internal ordering of left and right themselves. We minus 1 from the result because we don't count the original ordering.
'''




import math
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 1000000007

        def dfs(nums):
            if len(nums) < 3:
                return 1
            left = [i for i in nums if i < nums[0]]
            right = [i for i in nums if i > nums[0]]

            return dfs(left) * dfs(right) * math.comb(len(nums) - 1, len(left)) % mod

        return (dfs(nums) - 1) % mod

# Time complexity = O(n^2) where n is the size of nums
# Space complexity = O(n)
