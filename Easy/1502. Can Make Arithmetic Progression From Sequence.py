# easy

'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
'''

# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        progress = arr[1] - arr[0]

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != progress:
                return False

        return True

# Time complexity = O(nlogn) where n is the length of arr
# Space complexity = O(n)


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        maxi = max(arr)
        mini = min(arr)
        n = len(arr)

        if (maxi - mini) % (n - 1):
            return False

        progress = (maxi - mini) // (n - 1)
        i = 0

        while i < n:
            if arr[i] == mini + i * progress:
                i += 1
            elif (arr[i] - mini) % progress:
                return False
            else:
                tar = (arr[i] - mini) // progress

                if arr[i] == arr[tar]:
                    return False

                arr[i], arr[tar] = arr[tar], arr[i]

        return True

# Time complexity = O(n)
# Space complexity = O(1)
