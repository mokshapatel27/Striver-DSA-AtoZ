#https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1

class Solution:
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        current = head
        
        while current is not None:
            if current.data == x:
                next_node = current.next  # Save next node before breaking links
                
                # If the node to be deleted is the head node
                if current == head:
                    head = current.next
                
                # Adjust the pointer of the previous node
                if current.prev is not None:
                    current.prev.next = current.next
                    
                # Adjust the pointer of the next node
                if current.next is not None:
                    current.next.prev = current.prev
                    
                current = next_node
            else:
                current = current.next
                
        return head
