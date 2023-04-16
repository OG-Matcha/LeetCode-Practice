# medium
# https://leetcode.com/problems/jump-game-vi/

'''
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. 
In one move, you can jump at most k steps forward without going outside the boundaries of the array. 
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). 
Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.
'''

# Monotonic queue
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        deq, n = deque([0]), len(nums)

        for i in range(1, n):
            while deq and deq[0] < i - k: 
                deq.popleft()
                
            nums[i] += nums[deq[0]]
            
            while deq and nums[i] >= nums[deq[-1]]: 
                deq.pop()
                
            deq.append(i)
            
        return nums[-1]

# Time complexity = O(n)
# Space complexity = O(1)