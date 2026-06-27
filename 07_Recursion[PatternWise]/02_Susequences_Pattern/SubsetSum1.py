#https://www.geeksforgeeks.org/problems/introduction-to-dp/1

class Solution:
    # 1. Top-Down Approach
    def topDown(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
            
        # Base Cases
        if n == 0: return 0
        if n == 1: return 1
        
        # Return if already calculated
        if n in memo:
            return memo[n]
            
        MOD = 10**9 + 7
        
        # Recursive Step
        memo[n] = (self.topDown(n - 1, memo) + self.topDown(n - 2, memo)) % MOD
        return memo[n]

    def bottomUp(self, n: int) -> int:
        if n <= 1: return n
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
            
        return dp[n]
