#https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1

'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        new=Node(x)
        
        if head is None:
            return new
            
        current=head
        while current.next is not None:
            current=current.next
            
        current.next=new
        return head
