# easy

'''
Given two binary strings a and b, return their sum as a binary string.
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{(int(a, 2) + int(b, 2)):b}"
