# medium

'''
You are assigned to put some amount of boxes onto one truck. 
You are given a 2D array boxTypes, 
where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

• numberOfBoxesi is the number of boxes of type i.
• numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
'''

# Sort
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        res = 0
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        
        for box in boxTypes:
            
            if truckSize >= box[0]:
                truckSize -= box[0]
                res += box[0] * box[1]
            else:
                while truckSize > 0 and box[0] > 0:
                    truckSize -= 1
                    box[0] -= 1
                    res += box[1]
                
        return res
        
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        res = 0
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        
        for box in boxTypes:
            
            box[0] = min(truckSize, box[0])
            res += box[0] * box[1]
            truckSize -= box[0]
                
        return res

# Time complexity = O(nlogn)
# Space complexity = O(n)