# medium

'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''

# Binary Search

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def check(mid):
            return sum(ceil(p / mid) for p in piles) <= h  # (slower)
            # return sum((p + mid - 1) / mid for p in piles) <= h (faster)

        while left < right:
            mid = (left + right) // 2

            if not check(mid):
                left = mid + 1
            else:
                right = mid

        return left

# Time compexity = O(nlog(maxP))
# Space complexity = O(1)
