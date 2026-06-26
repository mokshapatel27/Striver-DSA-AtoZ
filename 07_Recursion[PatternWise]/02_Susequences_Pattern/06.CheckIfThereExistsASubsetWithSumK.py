#https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

class Solution:
    def isSubsetSum (self, arr, sum):
        dp=[True]+[False]*sum
        
        for num in arr:
            for j in range(sum,num-1,-1):
                dp[j]=dp[j]or dp[j-num]
        return dp[sum]
