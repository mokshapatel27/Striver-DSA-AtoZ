#https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

class Solution:
    def kthElement(self, a, b, k):
        n,m=len(a),len(b)
        if n>m:
            return self.kthElement(b,a,k)
    
        low,high=max(0,k-m),min(n,k)
        
        while low<=high:
            i=(low+high)//2
            j=k-i
            
            l1=a[i-1] if i>0 else float('-inf')
            l2=b[j-1]if j>0 else float('-inf')
            r1=a[i]if i<n else float('inf')
            r2=b[j]if j<m else float('inf')
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
                
            elif l1>r2:
                high=i-1
            else:
                low=i+1
                
        return 0
