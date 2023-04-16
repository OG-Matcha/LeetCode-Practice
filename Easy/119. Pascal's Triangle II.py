# easy

'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        num = [[1], [1, 1], [1, 2, 1]]
        
        if rowIndex < 3:
            return num[rowIndex]
        
        while len(num) != rowIndex + 1:
            last = num[-1]
            temp = []
            for i in range(len(num) - 1):
                temp.append(last[i] + last[i + 1])
            num.append([1] + temp + [1])
        
        return num[rowIndex]