# easy

'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = [[] for i in range(numRows)]
        
        result[0].append(1)
        
        for i in range(1,numRows):
            result[i].append(1)
            n = len(result[i-1])
            for j in range(1,n):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)
        return result

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        num = [[1], [1, 1], [1, 2, 1]]
        
        if numRows < 4:
            return num[:numRows]
        
        while len(num) != numRows:
            last = num[-1]
            temp = []
            for i in range(len(num) - 1):
                temp.append(last[i] + last[i + 1])
            num.append([1] + temp + [1])
        
        return num