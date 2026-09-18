#https://www.geeksforgeeks.org/problems/graph-and-vertices/1

class Solution:
    def count(self, n):
        e=n*(n-1)//2
        
        return 1<< e
        
