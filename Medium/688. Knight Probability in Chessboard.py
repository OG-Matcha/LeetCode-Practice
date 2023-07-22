# medium

'''
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.
'''

# https://leetcode.com/problems/knight-probability-in-chessboard/description/


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        moves = [[-2, -1], [-2, 1], [-1, -2],
                 [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

        for move in range(1, k + 1):
            new_dp = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for m in moves:
                        new_r = r + m[0]
                        new_c = c + m[1]
                        if 0 <= new_r < n and 0 <= new_c < n:
                            new_dp[r][c] += dp[new_r][new_c] / 8
            dp = new_dp

        probability = 0

        for r in range(n):
            for c in range(n):
                probability += dp[r][c]

        return probability

# Time complexity = O(n^2 * k)
# Space complexity = O(n^2 * k)
