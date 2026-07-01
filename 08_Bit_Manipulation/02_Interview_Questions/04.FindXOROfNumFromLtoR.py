#https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

class Solution:
    def findXOR(self, l, r):
        '''if N(mod4)==0->N
        if N(mod4)==1->1
        if N(mod4)==2->N+1
        if N(mod4)==3->0'''
        
        
        xor=lambda n:[n,1,n+1,0][n%4]
        
        return xor(r)^xor(l-1)
        
