#https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        
        # Iterate over all possible starting points of substrings
        for i in range(n):
            # Frequency array for lowercase English letters (a-z)
            freq = [0] * 26
            
            # Extend the substring from index i to j
            for j in range(i, n):
                # Update the frequency of the current character
                freq[ord(s[j]) - ord('a')] += 1
                
                # Find max and min frequencies among characters that actually appeared
                max_f = 0
                min_f = float('inf')
                
                for f in freq:
                    if f > 0:
                        if f > max_f:
                            max_f = f
                        if f < min_f:
                            min_f = f
                
                # Add the beauty of the current substring to the total
                total_beauty += (max_f - min_f)
                
        return total_beauty
