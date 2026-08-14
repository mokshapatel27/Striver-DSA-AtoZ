#https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
#left properly
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs=sorted(zip(profit,deadline),reverse=True)
        
        maxdeadline=max(deadline)
        
        slots=[False]*(maxdeadline+1)
        count=0
        maxprofit=0
        
        for p,d in jobs:
            for slot in range(d,0,-1):
                if not slots[slot]:
                    slots[slot]=True
                    count+=1
                    maxprofit+=p
                    break
        return [count,maxprofit]
