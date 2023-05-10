# medium

'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

# https://leetcode.com/problems/spiral-matrix-ii/description/


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        left = 0
        right = n - 1
        up = 0
        down = n - 1
        num = 1

        ans = [[0] * n for _ in range(n)]

        while left < right and up < down:

            for i in range(left, right):
                ans[up][i] = num
                num += 1
            for i in range(up, down):
                ans[i][right] = num
                num += 1
            for i in range(right, left, -1):
                ans[down][i] = num
                num += 1
            for i in range(down, up, -1):
                ans[i][left] = num
                num += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        if n & 1:
            ans[n // 2][n // 2] = num

        return ans

# Time complexity = O(n^2) where n is given input and we are iterating over n * n matrix in spiral form.
# Space Complexity: O(1)
