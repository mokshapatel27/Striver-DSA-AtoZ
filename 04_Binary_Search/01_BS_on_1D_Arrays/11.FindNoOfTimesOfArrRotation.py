#https://www.geeksforgeeks.org/problems/rotation4723/1

class Solution:
    def findKRotation(self, arr):
        # code here
        low=0
        high=len(arr)-1
        
        if arr[low]<=arr[high]:
            return 0
        
        while low<=high:
            mid=(low+high)//2
            
            if mid<high and arr[mid]>arr[mid+1]:
                return mid+1
            if mid>low and arr[mid]<arr[mid-1]:
                return mid
                
            if arr[mid]>=arr[low]:
                low=mid+1
            else:
                high=mid-1
                
        return 0
