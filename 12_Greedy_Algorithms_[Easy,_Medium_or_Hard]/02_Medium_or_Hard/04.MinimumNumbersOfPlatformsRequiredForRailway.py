#https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        
        n=len(arr)
        arr.sort()
        dep.sort()
        
        i,j=0,0
        count=0
        maxplatforms=0
        
        while i<n and j<n:
            if arr[i]<=dep[j]:
                count+=1
                maxplatforms=max(maxplatforms,count)
                i+=1
            else:
                count-=1
                j+=1
        return maxplatforms
