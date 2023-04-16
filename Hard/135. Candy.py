# hard
# https://leetcode.com/problems/candy/

'''
There are n children standing in a line. 
Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

• Each child must have at least one candy.
• Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.
'''

# One array
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        ans = [1] * len(ratings)
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])
                
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                ans[i] = max(1 + ans[i+1], ans[i])
        
        return sum(ans)

# Time complexity = O(N)
# Space complexity = O(N)