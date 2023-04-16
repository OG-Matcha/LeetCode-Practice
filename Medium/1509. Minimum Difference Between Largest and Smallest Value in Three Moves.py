# medium

'''
You are given an integer array nums. 
In one move, you can choose one element of nums and change it by any value.

Return the minimum difference between the largest and smallest value of nums after performing at most 
three moves.
'''

class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) < 5:
            return 0
        
        maxi, mini = [-inf] * 4, [inf] * 4
        
        for n in nums:
            
            if n > maxi[0]:
                maxi[0] = n
                
                for i in range(0, 3):
                    if maxi[i] > maxi[i + 1]:
                        maxi[i], maxi[i + 1] = maxi[i + 1], maxi[i]
                        
            if n < mini[0]:
                mini[0] = n
                
                for i in range(0, 3):
                    if mini[i] < mini[i + 1]:
                        mini[i], mini[i + 1] = mini[i + 1], mini[i]
        
        return min(maxi[i] - mini[3 - i] for i in range(4))

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        
        nums.sort()
        
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])