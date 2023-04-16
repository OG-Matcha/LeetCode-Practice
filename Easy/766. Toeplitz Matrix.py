# easy

'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
'''

# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        data = {}
        
        for ridx, row in enumerate(matrix):
            for cidx, val in enumerate(row):
                if ridx - cidx not in data:
                    data[ridx - cidx] = val
                if data[ridx - cidx] != val:
                    return False
        
        return True

# Time complexity = O(m * n)
# Space complexity = O(m + n)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        data = matrix[0]
        
        for row in matrix[1:]:
            data.pop()
            data.insert(0, row[0])
            if data != row:
                return False
        return True

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
    
class Solution:    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True