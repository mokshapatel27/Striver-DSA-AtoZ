#https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1
'''maxheap:

class Solution:
    def isMaxHeap(self, arr):
        n=len(arr)
        
        for i in range(n):
            left=2*i+1
            right=2*i+2
                
            if left<n and arr[i]<arr[left]:
                return False
            if right<n and arr[i]<arr[right]:
                return False
                
        return True
        '''

class Solution:
    def isMinHeap(self, arr):
        n = len(arr)
        
        # Only need to check internal nodes that have children
        for i in range((n - 1) // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            
            # If left child exists and is smaller than parent
            if left < n and arr[i] > arr[left]:
                return False
                
            # If right child exists and is smaller than parent
            if right < n and arr[i] > arr[right]:
                return False
                
        return True
