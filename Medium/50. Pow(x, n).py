# medium

'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            return self.myPow(1 / x, -n)
        
        if n == 0:
            return 1

        if n % 2 == 0:
            y = self.myPow(x, n / 2)
            return y * y
        
        if n % 2 == 1:
            y = self.myPow(x, n // 2)
            return y * y * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        pow = self.cal(x, n//2)

        if n % 2 == 1:
            return pow * pow * x
        else:
            return pow * pow 
    
    def cal(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n
        return self.myPow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n