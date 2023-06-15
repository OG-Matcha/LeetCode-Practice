# medium

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

# https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, v in enumerate(nums):

            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = v + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([v, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res

# Time complexity = O(n^2)
# Space complexity = O(1)
