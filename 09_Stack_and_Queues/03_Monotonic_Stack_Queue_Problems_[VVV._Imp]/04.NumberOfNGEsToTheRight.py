#https://www.geeksforgeeks.org/problems/number-of-nges-to-the-right/1

class Solution:
    def countGreater(self, arr, indices):
        res=[]
        
        for idx in indices:
            count=0
            #target value which we're comparing against
            #(Stores the value at the current query index into a variable called target.)
            target=arr[idx]
            for i in range(idx+1,len(arr)):
                if arr[i]>target:
                    count+=1
            res.append(count)
            
        return res
