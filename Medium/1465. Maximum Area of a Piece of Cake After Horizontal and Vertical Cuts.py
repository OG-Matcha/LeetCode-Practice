# medium

'''
You are given a rectangular cake of size h x w 
and two arrays of integers horizontalCuts and verticalCuts where:

• horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and 
  similarly, and
• verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position 
provided in the arrays horizontalCuts and verticalCuts. 
Since the answer can be a large number, return this modulo 109 + 7.
'''

# Sort
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        height = [0] + sorted(horizontalCuts) + [h]
        width = [0] + sorted(verticalCuts) + [w]
        
        max_height = max(height[i+1] - height[i] for i in range(len(height)-1))
        max_width = max(width[i+1] - width[i] for i in range(len(width)-1))
        
        return (max_height * max_width) % (10 ** 9 + 7)

# Time complexity = O(hlogh + wlogw)
# Space complexity = O(w + h)