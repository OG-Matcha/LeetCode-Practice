# medium

'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #get number of rows in the matrix
        m = len(matrix)

        #get number of coloumn in the matrix
        n = len(matrix[0])

        #set boundaries
        left = 0
        right = n - 1
        up = 0
        down = m - 1

        #set an empty list
        res = []

        #traverse though matrix untill all elements are met
        while len(res) < (m * n):
            #traverse from left to right on top
            if up <= down:
                for j in range(left, right + 1):
                    res.append(matrix[up][j])
                up += 1

            #traverse from up to down on the right side
            if left <= right:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1

            #traverse from right to left on bottom
            if up <= down:
                for j in reversed(range(left, right + 1)):
                    res.append(matrix[down][j])
                down -= 1

            #traverse from down to up on the left side
            if left <= right:
                for i in reversed(range(up, down + 1)):
                    res.append(matrix[i][left])
                left += 1

        return res