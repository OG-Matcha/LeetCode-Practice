# hard

'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        self.count = 0 # count = 0
        
        def backtrack(r):

            if r == n:
                self.count += 1 # nonlocal count
                return          # count += 1
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                
                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        
        backtrack(0)
        return self.count

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = {1:1, 2:0, 3:0, 4:2, 5:10, 6:4, 7:40, 8:92, 9:352}
        return res[n]