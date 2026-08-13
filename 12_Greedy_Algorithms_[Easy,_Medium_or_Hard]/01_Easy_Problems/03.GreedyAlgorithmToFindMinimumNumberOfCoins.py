#https://www.geeksforgeeks.org/problems/number-of-coins1824/1
#LEFT

class Solution:
    def minCoins(self, coins: list[int], sum: int) -> int:
        # dp[i] will hold the minimum coins needed for sum 'i'
        # Initialize array with infinity (or sum + 1)
        dp = [float('inf')] * (sum + 1)
        
        # Base case: 0 coins are needed to make sum 0
        dp[0] = 0
        
        # Build solution for every sum from 1 to 'sum'
        for i in range(1, sum + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
                    
        # Return answer if possible, otherwise -1
        return dp[sum] if dp[sum] != float('inf') else -1
