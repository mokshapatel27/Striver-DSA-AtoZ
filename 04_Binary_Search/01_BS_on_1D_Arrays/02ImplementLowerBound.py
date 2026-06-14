#https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

class Solution:
    def findFloor(self, arr, x):
        low=0
        high=len(arr)-1
        res=-1
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]<=x:
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res
