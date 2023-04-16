# medium

'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''

class Solution:
    def numSquares(self, n: int) -> int:
        square = set()
        
        for i in range(1, int(n ** 0.5) + 1):
            square.add(i * i)
            
        result = square.copy()
        count = 1
        
        while n not in result:
            for i in result.copy():
                for j in square:
                    if i + j <= n:
                        result.add(i + j)
            count += 1
            
        return count

# Brute Force
class Solution:
    def numSquares(self, n: int) -> int:
       square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
       
       def minNumSquares(k):
           if k in square_nums:
               return 1
           
           min_num = float('inf')
           
           for square in square_nums:
               if k < square:
                   break
               new_num = minNumSquares(k - square) + 1
               min_num = min(min_num, new_num)
           return min_num
       
       return minNumSquares(n)
# Time: TLE
# Space: SO
    
    
# Dynammic Programming
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp =  [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
                
        return dp[-1]
# Time: O(n * sqrt(n))
# Space: O(N)


# Greedy (DFS)
class Solution:
    def numSquares(self, n: int) -> int:
       def is_divided_by(n, count):
           if count == 1:
               return n in square_nums
           
           for k in square_nums:
               if is_divided_by(n - k, count - 1):
                   return True
           return False
       
       square_nums = set([i**2 for i in range(1, int(math.sqrt(n)) + 1)])
           
       for count in range(1, n + 1):
           if is_divided_by(n, count):
               return count
           
# Time: O(n^(1/(h+1)) - 1 / sqrt(n) - 1) ==> O(n^(h/2)), where h = max recursions
# Space: O(sqrt(n))
    
# Greedy + BFS
class Solution:
    def numSquares(self, n: int) -> int:
       square_nums = set([i**2 for i in range(1, int(math.sqrt(n)) + 1)])
       
       level = 0
       queue = {n}
       while queue:
           level += 1
           next_queue = set()
           for remainder in queue:
               for square_num in square_nums:
                   if remainder == square_num:
                       return level
                   elif remainder > square_num:
                       next_queue.add(remainder - square_num)
                       
           queue = next_queue
       return level
# Time: O(n^(1/(h+1)) - 1 / sqrt(n) - 1) ==> O(n^(h/2)), where h = height of n-ary tree
# Space: O(n^(1/h))
    
# Math
class Solution:
    def isSquare(self, n):
        sq = int(math.sqrt(n))
        return sq ** 2 == n
    
    def numSquares(self, n: int) -> int:
        while (n & 3) == 0:
            n >>= 2
        if (n & 7) == 7:
            return 4
        
        if self.isSquare(n):
            return 1
        for i in range(1, int(math.sqrt(n) + 1)):
            if self.isSquare(n - i**2):
                return 2
            
        return 3
        
#Time: O(sqrt(n))
#Space: O(1)