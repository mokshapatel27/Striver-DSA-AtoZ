#https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1

class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        return heapq.nsmallest(k,arr)[-1]
