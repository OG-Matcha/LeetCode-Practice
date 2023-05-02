# easy

'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
'''

# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/


class Solution:
    def arraySign(self, nums: List[int]) -> int:

        sign = 1

        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                sign *= -1

        return sign

# Time complexity = O(n) where n is the number of the elements in nums
# Space complexity = O(1)
