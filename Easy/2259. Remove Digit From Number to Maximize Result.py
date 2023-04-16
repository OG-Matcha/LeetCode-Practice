# easy

'''
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number 
such that the value of the resulting string in decimal form is maximized. 
The test cases are generated such that digit occurs at least once in number.
'''

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = []
        
        for i in range(len(list(number))):
            curr = list(number)
            if number[i] == digit:
                curr[i] = ""
                result.append("".join(curr))
        
        return max(result)

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return max(number[:i] + number[i + 1:] for i in range(len(number)) if number[i] == digit)

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = []
        
        for i, num in enumerate(number):
            if num == digit:
                result.append(number[:i] + number[i+1:])
        
        return max(result)