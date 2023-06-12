# easy

'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

• "a->b" if a != b
• "a" if a == b
'''

# https://leetcode.com/problems/summary-ranges/editorial/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        curr = []
        result = []

        for i in nums:
            
            if not curr or i - 1 == curr[-1]:
                curr.append(i)
            elif len(curr) == 1:
                result.append(str(curr[0]))
                curr = [i]
            else:
                result.append(str(curr[0]) + "->" + str(curr[-1]))
                curr = [i]
        
        if len(curr) == 1:
            result.append(str(curr[0]))
        elif len(curr) > 1:
            result.append(str(curr[0]) + "->" + str(curr[-1]))
        
        return result

# Time complexity = (n) where n is the length of the nums
# Space complexity = (n)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res = []
        i = 0

        while i < len(nums):
            curr = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            if curr != nums[i]:
                res.append(f"{curr}->{nums[i]}")
            else:
                res.append(f"{curr}")
            
            i += 1
        
        return res

# Time complexity = O(n)
# Space complexity = O(1)