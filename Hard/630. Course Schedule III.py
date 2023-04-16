# hard

'''
There are n different online courses numbered from 1 to n. 
You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be 
taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.
'''

# Heap
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        pq = []
        start = 0
        
        for dura, dead in sorted(courses, key= lambda c: c[1]):
            start += dura
            heapq.heappush(pq, -dura)
            
            if start > dead:
                start += heapq.heappop(pq)
        
        return len(pq)

# Time complexity = O(nlogn) 
# Space complexity = O(n)

# Greedy priority queue
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        t, h = 0, []
        for dur, due in courses:
            if t + dur <= due:
                heapq.heappush(h, -dur)
                t += dur
            elif h and -h[0] > dur:
                t += dur + heapq.heapreplace(h, -dur)
        return len(h)

# Time complexity = O(N)