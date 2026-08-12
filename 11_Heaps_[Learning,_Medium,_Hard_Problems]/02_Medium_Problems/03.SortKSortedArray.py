#https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1

class Solution:
    def mergeArrays(self, mat):
        return list(heapq.merge(*mat))
        
