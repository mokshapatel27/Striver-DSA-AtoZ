#https://www.geeksforgeeks.org/problems/shortest-job-first/1

class Solution:
    def solve(self, bt):
        bt.sort()
        totalwait=0
        waittime=0
        
        for t in bt:
            totalwait+=waittime
            waittime+=t
            
        return totalwait//len(bt)
        
