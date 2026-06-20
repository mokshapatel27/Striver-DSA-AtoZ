#https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1

"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        
        #c1:x=head node del that
        
        if x==1:
            head=head.next
            if head:
                head.prev=None
            return head
            
        #c2:traverse to node at pos x
        curr=head
        for _ in range(x-1):
            curr=curr.next
        if curr.prev:
                curr.prev.next=curr.next
                
        if curr.next:
                curr.next.prev=curr.prev
        return head
