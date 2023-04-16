# easy

'''
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
'''

# Brute-force
class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            ans += i
            if ans == n:
                return i
            elif ans > n:
                return i - 1

# Binary-search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        result = 0

        while left <= right:
            mid = (left + right) // 2

            ans = (mid * (mid + 1)) // 2

            if ans == n:
                return mid
            elif ans > n:
                right = mid - 1
            else:
                left = mid + 1
                result = mid
                
        return result