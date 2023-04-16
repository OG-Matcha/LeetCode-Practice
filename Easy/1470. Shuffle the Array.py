# easy

'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''

# https://leetcode.com/problems/shuffle-the-array/description/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n]
        right = nums[n:]
        res = []

        for i in range(n):
            res.append(left[i])
            res.append(right[i])

        return res


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i, j in zip(nums[:n], nums[n:]):
            res += [i, j]

        return res

# Time complexity = O(n)
# Space complexity = O(n)
