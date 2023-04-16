# medium

'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        data = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in data:
                    data[i + j] = [mat[i][j]]
                else:
                    data[i + j].append(mat[i][j])
                    
        result = []
        
        for i in data.items():
            if i[0] % 2 == 0:
                [result.append(j) for j in i[1][::-1]]
            else:
                [result.append(j) for j in i[1]]
        
        return result