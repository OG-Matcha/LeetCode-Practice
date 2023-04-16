# easy

'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        result = []
        
        for i in range(len(matrix[0])):
            
            curr = [] # result.append([matrix[j][i] for j in range(len(matrix))])
            
            for j in range(len(matrix)):
                curr.append(matrix[j][i])
                
            result.append(curr)
            
        return result

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        res = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                res[i][j] = matrix[j][i]
                
        return res