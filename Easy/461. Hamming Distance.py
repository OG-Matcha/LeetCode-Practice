# easy

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits 
are different.

Given two integers x and y, return the Hamming distance between them.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        def countone(n):
            count = 0
            while n > 0:
                if n != 0:
                    n = n & (n - 1)
                    count += 1
            return count
        
        return countone(x ^ y)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        c = Counter(str(bin(diff)))
        return c['1']