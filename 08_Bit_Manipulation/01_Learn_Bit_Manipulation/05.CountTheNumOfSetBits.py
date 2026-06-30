#https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
#O(logn),O(1)

class Solution:
    def countSetBits(self,n):
        #to incl 0
        n+=1
        setbits=0
        
        #tracks current bit(0th) pos as pow of 2
        twopow=1
        
        #loops thru all bits
        while twopow<n:
            #calculates complete cycle of 0s and 1s fir current bit pos
            
            total=n//(twopow*2)
            setbits+=total*twopow
            #finds how many nos. are left, handles extra 1s in incomplete cycle
            remainder=n%(twopow*2)
            if remainder>twopow:
                setbits+=remainder-twopow
            twopow*=2
        return setbits
