#https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1


class Solution:
    def jobSequencing(self, deadline, profit):
        #pairs each profit with its deadline and sorts as highest profit first
        jobs=sorted(zip(profit,deadline),reverse=True)
        
        #tells us the total number of slots that we need
        maxdeadline=max(deadline)
        
        #creates a boolean list with all deadlines installed as false in the start 
        slots=[False]*(maxdeadline+1)
        count=0
        maxprofit=0
        
        for p,d in jobs:
            #Searches backward from the job's deadline d down to 1.
            #Why backward? We greedily schedule a job as late as possible (at or near its deadline) so that earlier slots remain free for jobs with tighter deadlines.
            for slot in range(d,0,-1):
                if not slots[slot]:
                    slots[slot]=True
                    count+=1
                    maxprofit+=p
                    break
        return [count,maxprofit]
