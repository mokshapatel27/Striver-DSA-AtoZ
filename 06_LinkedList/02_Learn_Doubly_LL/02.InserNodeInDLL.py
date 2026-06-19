#https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1

class Solution:
    def insertAtPos(self, head, p, x):
        # Step 1: Traverse to the p-th node
        curr = head
        for _ in range(p):
            if curr:
                curr = curr.next
                
        if not curr:
            return head
            
        # Step 2: Create the new node
        new_node = Node(x)
        
        # Step 3: Adjust the pointers to insert the new node
        new_node.next = curr.next
        new_node.prev = curr
        
        if curr.next:
            curr.next.prev = new_node
            
        curr.next = new_node
        
        return head
