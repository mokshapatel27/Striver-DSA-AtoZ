#https://www.naukri.com/code360/problems/allocate-books_1090540?leftPanelTabValue=SUBMISSION

def findPages(arr: [int], n: int, m: int) -> int:
    if m>n:
        return -1

    low=max(arr)
    high=sum(arr)
    ans=-1

    while low<=high:
        mid=(low+high)//2

        studens=1
        currpgs=0
        possibility=True  

        for pages in arr:
            if currpgs+pages<=mid:
                currpgs+=pages
            else:
                studens+=1
                currpgs=pages

                if studens>m:
                    possibility=False
                    break
                
        if possibility:
            ans=mid
            high=mid-1
        else:
            low=mid+1
        
    return ans
