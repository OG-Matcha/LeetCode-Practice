# medium

'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day 
to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        length = len(temperatures)
        hottest = 0
        answer = [0] * length
        
        for currentDay in range(length - 1, -1, -1):
            currentTemperature = temperatures[currentDay]
            
            if currentTemperature >= hottest:
                hottest = currentTemperature
                continue
            
            days = 1
            
            while temperatures[currentDay + days] <= currentTemperature:
                days += answer[currentDay+ days]
                
            answer[currentDay] = days
            
        return answer
                
# Time complexity = O(n)
# Space complexity = O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        lst = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            
            if len(stack) == 0:
                lst.append(0)
            
            elif len(stack) > 0 and stack[-1][0] > temperatures[i]:
                lst.append(stack[-1][1] - i)
            
            elif len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                
                while len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                    
                if len(stack) == 0:
                    lst.append(0)
                    
                else:
                    lst.append(stack[-1][1] - i)
                    
            stack.append([temperatures[i], i])
            
        return lst[::-1]
            