#https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        new=sorted(set(arr))
        low=0
        high=len(new)-1
        floor=-1
        ceil=-1
        while low<=high:
            mid=(low+high)//2
            
            if new[mid]==x:
                return[new[mid],new[mid]] #both floor ans ceil
                
            elif new[mid]<x:
                floor=new[mid]
                low=mid+1
            else:
                ceil=new[mid]
                high=mid-1
                
        return [floor,ceil]
                        
