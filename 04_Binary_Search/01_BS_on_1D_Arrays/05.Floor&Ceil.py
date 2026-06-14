#https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=SUBMISSION

def getFloorAndCeil(a, n, x):
        low=0
        high=n-1
        floor=-1
        ceil=-1
        while low<=high:
            mid=(low+high)//2
            
            if a[mid]==x:
                return[a[mid],a[mid]] #both floor ans ceil
                
            elif a[mid]<x:
                floor=a[mid]
                low=mid+1
            else:
                ceil=a[mid]
                high=mid-1
                
        return [floor,ceil]
