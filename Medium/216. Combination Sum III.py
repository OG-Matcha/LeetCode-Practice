# medium

'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. 
The list must not contain the same combination twice, and the combinations may be returned in any order.
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        perm = list(permutations([i for i in range(1,10)], k))
        result = []
        
        for i in perm:
            if (sum(i) == n) and (sorted(i) not in result):
                result.append(sorted(i))
        return result
    
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [x for x in list(combinations([i for i in range(1,10)], k)) if sum(x) == n]