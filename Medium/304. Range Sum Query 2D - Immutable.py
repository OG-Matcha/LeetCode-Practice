# medium

# https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/

'''
Given a 2D matrix matrix, handle multiple queries of the following type:

• Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) 
and lower right corner (row2, col2).

Implement the NumMatrix class:

• NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) 
• Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) 
and lower right corner (row2, col2).
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.preSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.preSum[i][j] = self.preSum[i - 1][j] + self.preSum[i][j - 1] + matrix[i - 1][j - 1] - self.preSum[i - 1][j - 1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.preSum[row2][col2] - self.preSum[row2][col1 - 1] - self.preSum[row1 - 1][col2] + self.preSum[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)