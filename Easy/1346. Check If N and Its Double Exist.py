# easy

'''
Given an array arr of integers, 
check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

▪ i != j
▪ 0 <= i, j < arr.length
▪ arr[i] == 2 * arr[j]
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i == 0:
                count += 1
            if (i != 0) & (i * 2 in arr):
                return True
        return count > 1

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if (i != 0) & (i * 2 in arr):
                return True
        return arr.count(0) > 1