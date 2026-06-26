#LEFT
#http://geeksforgeeks.org/problems/better-string/1


class Solution:
    def betterString(self, s1: str, s2: str) -> str:
        counts = []
        
        # Calculate distinct subsequences for both strings
        for s in (s1, s2):
            n = len(s)
            dp = [0] * (n + 1)
            dp[0] = 1 # Empty string base case
            
            last_pos = {}
            for i in range(1, n + 1):
                char = s[i - 1]
                # Doubling the count of subsequences from the previous step
                dp[i] = 2 * dp[i - 1]
                
                # If character was seen before, remove duplicate subsequences
                if char in last_pos:
                    dp[i] -= dp[last_pos[char] - 1]
                
                last_pos[char] = i
                
            counts.append(dp[n])
        
        # Return s1 if it has more or equal number of distinct subsequences
        return s1 if counts[0] >= counts[1] else s2
