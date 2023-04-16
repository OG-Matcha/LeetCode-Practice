# easy

'''
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, 
you have to subtract 1 from it.
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        count = 0
        
        while num:
            
            if num % 2 == 0:
                num //= 2
                count += 1
            else:
                num -= 1
                count += 1
                
        return count

class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        count = 0
        
        while num:
            
            count += 1
            
            if num & 1:
                num -= 1
            else:
                num >>= 1
                
        return count