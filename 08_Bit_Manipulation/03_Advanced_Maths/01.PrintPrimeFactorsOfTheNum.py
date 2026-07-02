#https://www.geeksforgeeks.org/problems/prime-factors5052/1

class Solution:
    def primeFac(self, n):
        ans=[]
        i=2
        
        while i*i<=n:
            if n%i==0:
                ans.append(i)
                
                while n%i==0:
                    '''We actually divide n by i and shrink n down. 
                    For example, if n is $100$ and i is $2$, 
                    we divide by $2$ to get $50$, then divide by $2$ again to get $25$.'''
                    n//=i
            i+=1
        #After the loop finishes, we check our shrunken number n.
        if n>1:
            ans.append(n)
            
        return ans
