# medium

'''
You have a lock in front of you with 4 circular wheels. 
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def getNeighbor(lst):
            res = []
            for i in range(len(lst)):
                if lst[i] == "0":
                    res.append(lst[:i] + "1" + lst[i + 1:])
                    res.append(lst[:i] + "9" + lst[i + 1:])
                elif lst[i] == "9":
                    res.append(lst[:i] + "0" + lst[i + 1:])
                    res.append(lst[:i] + "8" + lst[i + 1:])
                else:
                    add = chr(ord(lst[i]) + 1)
                    sub = chr(ord(lst[i]) - 1)
                    
                    res.append(lst[:i] + add + lst[i + 1:])
                    res.append(lst[:i] + sub + lst[i + 1:])
            return res
                               
        deadends = set(deadends)
        start = "0000"
        q1 = []
        q1.append(start)
        q2 = []
        q2.append(target)
        
        if start in deadends:
            return -1
        
        visited = set()
        visited.add(start)
        
                               
        level = 0
        
        while (q1 and q2):
            temp = set()
            
            for i in range(len(q1)):
                cur = q1.pop()

                if cur in q2:
                    return level

                for neighbor in getNeighbor(cur):

                    if neighbor not in deadends:

                        if neighbor in q2:
                            return level + 1
                            
                        if neighbor not in visited:
                            temp.add(neighbor)
                            visited.add(neighbor)
            q1 = q2
            q2 = temp
            level += 1
        
        return -1

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        
        stack = [("0000",0)]
        
        while stack:
            move, turn = stack.pop(0)
            
            if move in deadends:
                continue
            deadends.add(move)
                
            if move == target:
                return turn
            
            for i in range(4):
                for d in (-1, 1):
                    next = move[:i] + str((int(move[i]) + d) % 10) + move[i + 1:]
                    stack.append((next, turn + 1))
            
        return -1