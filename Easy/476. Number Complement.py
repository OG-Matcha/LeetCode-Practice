# easy

'''
The complement of an integer is the integer you get when you flip all the 0's to 1's 
and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
'''

class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num)[2:])
        
        
        for i in range(len(binary)):
            binary[i] = str(int(binary[i]) ^ 1)
        
        return int("".join(binary), 2)

class Solution:
    def findComplement(self, num: int) -> int:
        check = "1" * (len(bin(num)) - 2)
        return num ^ int(check, 2)