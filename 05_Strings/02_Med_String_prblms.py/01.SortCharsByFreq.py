#https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count frequencies
        freq = Counter(s)
        res = []
        
        # Step 2: Loop through the most common elements
        for letter, count in freq.most_common():
            res.append(letter * count)
            
        # Step 3: Join and return the result
        return "".join(res)
