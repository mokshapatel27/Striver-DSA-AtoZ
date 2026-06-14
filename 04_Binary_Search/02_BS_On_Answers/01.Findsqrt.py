#https://www.geeksforgeeks.org/problems/square-root/1

class Solution:
    def floorSqrt(self, n): 
        # code here
        if n==0 or n==1:
            return n
            
        low,high,ans=1,n,0
        
        while low<=high:
            mid=(low+high)//2
            midsq=mid*mid
            
            if midsq==n:
                return mid
                
            if midsq<n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
                
        return ans
