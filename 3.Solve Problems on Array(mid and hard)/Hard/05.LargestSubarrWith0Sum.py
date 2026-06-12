#https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

class Solution:
    def maxLength(self, arr):
        
        prefixsum={}
        maxlen=0
        currsum=0
        
        for i,val in enumerate(arr):
            currsum+=val
            
            if currsum==0:
                maxlen=i+1
                
            elif currsum in prefixsum:
                maxlen=max(maxlen,i-prefixsum[currsum])
                
            else:
                prefixsum[currsum]=i
                
        return maxlen
