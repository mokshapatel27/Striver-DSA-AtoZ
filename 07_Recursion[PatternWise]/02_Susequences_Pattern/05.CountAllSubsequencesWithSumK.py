#https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

class Solution:
	def perfectSum(self, arr, target):
	    MOD=10**9+7
	    
	    dp=[0]*(target+1)
	    
	    dp[0]=1
	    
	    for num in arr:
	        for j in range(target,num-1,-1):
	            dp[j]=(dp[j]+dp[j-num])%MOD
        return dp[target]
