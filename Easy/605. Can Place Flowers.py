# easy

'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''

# https://leetcode.com/problems/can-place-flowers/submissions/918405497/


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros = 1
        ans = 0

        for i in flowerbed:
            if i == 0:
                zeros += 1
            else:
                ans += (zeros - 1) // 2
                zeros = 0

        return ans + zeros // 2 >= n


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1

                if n == 0:
                    return True

                flowerbed[i] = 1

        return False
