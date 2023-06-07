# medium

'''
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
'''

# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1:
                ans += 0 if ((a & 1) or (b & 1)) else 1
            else:
                ans += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count("1") + bin(a & b & ((a | b) ^ c)).count("1")

# Time complexity = O(n) where n is the maximum length in the binary representation of a, b or c
# Space complexity = O(n)


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()

# Time complexity = O(n)
# Time complexity = O(1)
