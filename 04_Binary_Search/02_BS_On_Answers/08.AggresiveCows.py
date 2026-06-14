#https://www.geeksforgeeks.org/problems/aggressive-cows/1

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
    
        low,high=1,stalls[-1]-stalls[0]
        
        while low<=high:
            mid=low+(high-low)//2
            
            placedcows=1
            pos=stalls[0]
            
            for i in range(1,len(stalls)):
                if stalls[i]-pos>=mid:
                    placedcows+=1
                    pos=stalls[i]
                    
            
            if placedcows>=k:
                low=mid+1
            else:
                high=mid-1
                
        return high
