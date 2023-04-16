# medium

'''
There are several cards arranged in a row, and each card has an associated number of points. 
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. 
You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        size = len(cardPoints) - k
        total = sum(cardPoints[size:])
        ans = total
        
        for i in range(0, k):
            total += cardPoints[i]
            total -= cardPoints[i+size]
            ans = max(ans, total)
        
        return ans

# Time complexity = O(K)
# Space complexity = O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        result = total
        
        while right < len(cardPoints):
            total += (cardPoints[left] - cardPoints[right])
            result = max(result, total)
            left += 1
            right += 1
            
        return result

# Time complexity = O(K)
# Space complexity = O(1)