# medium

'''
You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates 
the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points 
on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting 
adjacent points. One such example is shown below:
'''

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        
        if len(stockPrices) == 1:
            return 0
        
        stockPrices.sort()
        count = 1
        start = (stockPrices[1][1] - stockPrices[0][1]) // (stockPrices[1][0] - stockPrices[0][0])
        
        for i in range(1, len(stockPrices) - 1):
            curr = (stockPrices[i + 1][1] - stockPrices[i][1]) / (stockPrices[i + 1][0] - stockPrices[i][0])
            
            if curr != start:
                count += 1
                start = curr
                
        return count