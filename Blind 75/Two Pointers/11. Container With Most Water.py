# medium

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: List[int]) -> int:

        res = 0
        maxi = max(height)

        left = 0
        right = len(height) - 1

        while left < right:
            res = max(res, min(height[right], height[left]) * (right - left))

            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1

            if (right - left) * maxi <= res:
                break

        return res

# Time complexity = O(n) where n is the length of height
# Space complexity = O(1)
