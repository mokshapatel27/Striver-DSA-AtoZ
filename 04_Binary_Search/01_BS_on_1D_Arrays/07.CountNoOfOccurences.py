#https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        def bSearch(val):
            low,high=0,len(arr)-1
            while low<=high:
                mid=(low+high)//2
                
                if arr[mid]<val:
                    low=mid+1
                else:
                    high=mid-1
            return low
            
        return bSearch(target+1)-bSearch(target)
