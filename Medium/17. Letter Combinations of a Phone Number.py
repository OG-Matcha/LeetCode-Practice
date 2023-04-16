# medium

'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_alpha = {"2":["a","b","c"], 
                        "3":["d","e","f"], 
                        "4":["g","h","i"], 
                        "5":["j","k","l"], 
                        "6":["m","n","o"], 
                        "7":["p","q","r","s"], 
                        "8":["t","u","v"], 
                        "9":["w","x","y","z"]}
        
        def combine(proc):
            new_lst = []
            for i in range(len(proc)):
                new_lst.append("".join(proc[i]))
            return new_lst
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return number_alpha[digits]
        
        if len(digits) == 2:
            lst1 = number_alpha[digits[0]]
            lst2 = number_alpha[digits[1]]
            proc = list(product(lst1,lst2))
            return combine(proc)
            
        if len(digits) == 3:
            lst1 = number_alpha[digits[0]]
            lst2 = number_alpha[digits[1]]
            lst3 = number_alpha[digits[2]]
            proc = list(product(lst1,lst2,lst3))
            return combine(proc)
        
        if len(digits) == 4:
            lst1 = number_alpha[digits[0]]
            lst2 = number_alpha[digits[1]]
            lst3 = number_alpha[digits[2]]
            lst4 = number_alpha[digits[3]]
            proc = list(product(lst1,lst2,lst3,lst4))
            return combine(proc)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {"2": ["a", "b", "c"],
                  "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"],
                  "6": ["m", "n", "o"],
                  "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"],
                  "9": ["w", "x", "y", "z"]}
        
        results = []
        if not digits:
            return results

        def combine(i, res=""):
            if i == len(digits):
                results.append(res)
                return
            
            digit = digits[i]
            
            for letter in keypad[digit]:
                combine(i + 1, res + letter)
        
        combine(0, "")
        
        return results