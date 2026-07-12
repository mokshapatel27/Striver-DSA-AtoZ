#https://www.naukri.com/code360/problems/next-greater-element_1112581?leftPanelTabValue=SUBMISSION

def nextSmallerElement(arr,n):
    stack=[]
    #prefilled with -1 of size n
    ans=[-1]*n 

    for i in range(n-1,-1,-1):
        #if it is greater than i it can never be next smaller element hence pop
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            #only the genuine small elements left are stored
            ans[i]=stack[-1]

        stack.append(arr[i])
    return ans
