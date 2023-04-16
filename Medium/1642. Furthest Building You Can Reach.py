# medium

'''
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

• If the current building's height is greater than or equal to the next building's height, 
  you do not need a ladder or bricks.
• If the current building's height is less than the next building's height, 
  you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
'''

# Priority queue
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
            
        return len(heights) - 1

# Time complecity = O(NlogK)
# Space complecity = O(K)

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        gaps = []
        
        for i in range(len(heights)-1):
            gap = heights[i+1] - heights[i]
            
            if gap <= 0:
                continue
            
            if ladders > 0:
                ladders -= 1
                heapq.heappush(gaps, gap)
                continue
            
            if gaps and gaps[0] < gap:
                min_gap = heapq.heappop(gaps)
                if bricks >= min_gap:
                    bricks -= min_gap
                    heapq.heappush(gaps, gap)
                    continue
                else:
                    return i
            
            if gap <= bricks:
                bricks -= gap
            else:
                return i
                
        return i + 1