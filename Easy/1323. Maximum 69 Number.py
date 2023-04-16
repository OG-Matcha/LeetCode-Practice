# easy

'''
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
'''

# https://leetcode.com/problems/maximum-69-number/description/

class Solution:
    def maximum69Number (self, num: int) -> int:
        lst = list(str(num))
        for i in range(len(lst)):
            if lst[i] == "6":
                lst[i] = "9"
                break
        return "".join(lst)

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))

class Solution:
    def maximum69Number (self, num: int) -> int:
        six_index = -1
        remainder = num
        pos = 0

        while remainder:
            remainder, digit = divmod(remainder, 10)
            if digit == 6:
                six_index = pos
            pos += 1

        return num + 3 * 10 ** six_index if six_index >= 0 else num