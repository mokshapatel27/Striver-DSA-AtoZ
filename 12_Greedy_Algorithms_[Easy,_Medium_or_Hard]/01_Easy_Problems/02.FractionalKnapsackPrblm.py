#https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items=sorted(zip(val,wt),key=lambda item:item[0]/item[1],reverse=True)
        
        totalval=0.0
        
        for v,w in items:
            if capacity>=w:
                totalval+=v
                capacity-=w
            else:
                totalval+=(v/w)*capacity
                break
        return totalval
