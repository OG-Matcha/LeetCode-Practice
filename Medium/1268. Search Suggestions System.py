# medium

'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord 
is typed. Suggested products should have common prefix with searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
'''

# Brute-force
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        sort_pro = sorted(products)
        res = []
        
        for i in range(len(searchWord)):
            
            count = 0
            curr = []
            
            for pro in sort_pro:
                
                if pro.startswith(searchWord[:i+1]) and count < 3:
                    
                    curr.append(pro)
                    count += 1
                    
                elif count >= 3:
                    break
                    
            res.append(curr)
        
        return res

# Binary search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        ans = []
        start, end = 0, len(products)-1
        
        for i, c in enumerate(searchWord):
            
            while start <= end and (len(products[start]) <= i or products[start][i] < c):
                start += 1
            
            while start <= end and (len(products[end]) <= i or products[end][i] > c):
                end -= 1
            
            if start <= end:
                ans.append(products[start:min(start+3, end+1)])
            else:
                ans.append([])
        return ans

# Bitsect module
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        ans = []
        string = ""
        
        for c in searchWord:
            
            string += c
            i = bisect.bisect_left(products, string)
            ans.append([w for w in products[i: i + 3] if w.startswith(string)])
            
        return ans