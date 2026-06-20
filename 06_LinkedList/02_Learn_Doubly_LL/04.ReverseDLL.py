#https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

"""
Structure of doubly linked list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        
        if not head or not head.next:
            return head
            
        curr=head
        newh=None 
        
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            
            newh=curr
            curr=curr.prev
        return newh
