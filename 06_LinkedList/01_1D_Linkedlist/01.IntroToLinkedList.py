#https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1

'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def arrayToList(self, arr):
        # code here
        
        if not arr:
            return None 
            
        head=Node(arr[0])
        current=head
        
        for value in arr[1:]:
            current.next=Node(value)
            current=current.next
            
        return head
