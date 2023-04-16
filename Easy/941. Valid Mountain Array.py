# easy

'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

▪ arr.length >= 3
▪ There exists some i with 0 < i < arr.length - 1 such that:
    ▪ arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    ▪ arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        up = down = False
        temp = arr[0]
        
        for i in arr[1:]:
            if i == temp:
                return False
            
            if i > temp:
                if down:
                    return False
                up = True
            else:
                if not up:
                    return False
                down = True
            temp = i
        
        return up & down

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        i = 0
        
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1
        
        while i == 0 or i == len(arr) - 1:
            return False
        
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1
        
        return i == len(arr) - 1