#https://www.geeksforgeeks.org/problems/convert-an-array-to-reduced-form1101/1

class Solution:
    def replaceWithRank(self, arr):
        sortedpairs=sorted((val,i) for i,val in enumerate(arr))
        
        for rank,(val,orgidx) in enumerate(sortedpairs):
            arr[orgidx]=rank
