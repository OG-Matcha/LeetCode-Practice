# medium

'''
You are given an integer array nums and an integer x. In one operation, 
you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''

# Prefix sum & Sliding window

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        s = sum(nums)
        n = len(nums)
        goal = s - x
        max_length = -1
        left = 0
        current_sum = 0

        for right, num in enumerate(nums):
            current_sum += num

            while current_sum > goal and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == goal:
                max_length = max(max_length, right - left + 1)

        return n - max_length if max_length != -1 else -1