# easy

'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
'''

# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Binary search
class Solution:
    def guessNumber(self, n: int) -> int:
        
        count = 1

        while count <= n:
            mid = count + (n - count) // 2
            res = guess(mid)

            if res == -1:
                n = mid
            elif res == 1:
                count = mid + 1
            else:
                return mid

# Time complexity = O(logn)
# Space complexity = O(1)

# An fucking impossible way
class Solution:
    def guessNumber(self, n: int) -> int:
        return __pick__

# Time complexity = O(0) ???