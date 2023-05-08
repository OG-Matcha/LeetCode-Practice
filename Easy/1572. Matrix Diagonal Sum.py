# easy

'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''

# https://leetcode.com/problems/matrix-diagonal-sum/description/


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        length = len(mat)

        for i in range(length):
            total += mat[i][i] + mat[i][length - i - 1]

        if length & 1:
            total -= mat[length // 2][length // 2]

        return total


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        length = len(mat)
        left = 0
        right = length - 1

        for m in mat:
            if left == right:
                total += m[left]
            else:
                total += m[left] + m[right]

            left += 1
            right -= 1

        return total

# Time complexity = O(n)
# Time complexity = O(1)
