# medium

'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

# https://leetcode.com/problems/spiral-matrix/description/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1
        up = 0
        down = m - 1

        total = m * n
        ans = []

        while len(ans) < total:

            if up <= down:
                for i in range(left, right + 1):
                    ans.append(matrix[up][i])
                up += 1

            if left <= right:
                for i in range(up, down + 1):
                    ans.append(matrix[i][right])
                right -= 1

            if up <= down:
                for i in reversed(range(left, right + 1)):
                    ans.append(matrix[down][i])
                down -= 1

            if left <= right:
                for i in reversed(range(up, down + 1)):
                    ans.append(matrix[i][left])
                left += 1

        return ans

# Time complexity = O(m * n) where m is the length of columns and n is the length of rows
# Space complexity = O(1) without counting the answer


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        while matrix:
            ans += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return ans

# Time complexity = O(min(m, n) * m * n) where m is the length of columns and n is the length of rows
# Space complexity = O(1) without counting the answer
