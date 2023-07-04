# medium

'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

# https://leetcode.com/problems/single-number-ii/description/


''' Logical Thinking
The logical thinking behind this approach is to count the number of 1s at each bit position for all the numbers. Since each number appears three times except for the single number, the sum of 1s at each bit position should be divisible by 3 for a balanced line. Any number of 1s that is not divisible by 3 indicates an unbalanced line, which means the single number contributes to that particular bit position.

By masking the positions of the unbalanced lines with 1s in ans, we effectively isolate the bits that are part of the single number. Finally, the resulting value in ans represents the binary representation of the single number.

Using the provided example: [1, 1, 1, 2, 2, 2, 5]

At the LSB (i = 0), the sum of the number of 1s is 3 (balanced line).
At the second bit (i = 1), the sum of the number of 1s is 4 (unbalanced line, not divisible by 3).
At the third bit (i = 2), the sum of the number of 1s is 2 (unbalanced line, not divisible by 3).
At the fourth bit
(i = 3), the sum of the number of 1s is 1 (balanced line).

Thus, the resulting binary representation is '0101', which corresponds to the decimal value 5, and that is the single number we are searching for.

This approach effectively identifies the unbalanced lines and constructs the single number by setting the corresponding bit positions in ans.
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            bit_sum = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32 - 1)
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            ans |= bit_sum << i

        if ans >= 2**31:
            ans -= 2**32

        return ans

# Time complexity = O(32n) where n is the length of nums
# Time complexity = O(1)


''' Logical Thinking
The key idea is to use bitwise operations to keep track of the count of each bit position. By doing so, we can identify the bits that have appeared once, twice, or three times.

When a bit appears for the first time (ones is 0 and the bit is toggled), it is stored in ones.

When a bit appears for the second time (ones is 1 and the bit is toggled), it is removed from ones and stored in twos.

When a bit appears for the third time (ones is 0 and the bit is toggled), it is removed from both ones and twos.

By the end of the iteration, the bits that remain in ones represent the bits of the single number that appeared only once, while the bits in twos represent bits that appeared three times (which is not possible).

In summary, the algorithm uses bit manipulation to efficiently keep track of the counts of each bit position. By utilizing XOR and AND operations, it can identify the bits of the single number that appears only once in the array while ignoring the bits that appear multiple times.'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones

# Time complexity = O(n)
# Time complexity = O(1)
