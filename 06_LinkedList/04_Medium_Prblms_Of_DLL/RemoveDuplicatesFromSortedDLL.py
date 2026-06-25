#https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1

# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        if not headRef:
            return None
            
        curr=headRef
        
        while curr and curr.next:
            if curr.data==curr.next.data:
                duplicate=curr.next
                
                curr.next=duplicate.next
                
                if duplicate.next:
                    duplicate.next.prev=curr
                    
            else:
                curr=curr.next
        return headRef
       
