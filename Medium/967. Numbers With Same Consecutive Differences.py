# medium

'''
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.
'''

# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

# Bfs
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
    
        if n == 1:
            return [i for i in range(10)]
        
        queue = [i for i in range(1, 10)]
        
        for _ in range(n - 1):
            next_queue = []
            
            for num in queue:
                last_num = num % 10
                next_nums = set([last_num + k, last_num - k])
                
                for next_num in next_nums:
                    if 0 <= next_num < 10:
                        new_num = num * 10 + next_num
                        next_queue.append(new_num)
                
            queue = next_queue
            
        return queue

# Time complexity = O(2 ^ n)
# Space complexity = O(2 ^ n)

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        nums = [i for i in range(1, 10)]
        
        for _ in range(n - 1):
            res = []
            
            for num in nums:
                cur = num % 10
                
                if cur + k < 10:
                    res.append(num * 10 + cur + k)
                
                if k > 0 and cur - k >= 0:
                    res.append(num * 10 + cur - k)
        
            nums = res
        
        return res

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        cur = range(1, 10)
        
        for _ in range(n - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + k, x % 10 - k] if 0 <= y <= 9}
        
        return list(cur)