#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None:
            return []

        mapping = {
                '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
            }
        if len(digits)==1:
            return list(mapping[digits])
        prev=self.letterCombinations(digits[1:]) 
        return [letter+combo for letter in mapping[digits[0]] for combo in prev]   
