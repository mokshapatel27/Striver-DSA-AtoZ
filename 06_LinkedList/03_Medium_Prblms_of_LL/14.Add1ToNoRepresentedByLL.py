#https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
#LEFT

class Solution:
    def addOne(self, head):
        # Dummy node handles cases like 9 -> 9 -> 9 seamlessly
        dummy = Node(0)
        dummy.next = head
        
        last_not_nine = dummy
        curr = head
        
        # Traverse the list to find the rightmost node that is not 9
        while curr:
            if curr.data != 9:
                last_not_nine = curr
            curr = curr.next
            
        # Increment the rightmost non-9 node
        last_not_nine.data += 1
        
        # Change all subsequent 9s to 0s
        curr = last_not_nine.next
        while curr:
            curr.data = 0
            curr = curr.next
            
        # If the dummy node was incremented (e.g., 999 became 1000)
        if dummy.data == 1:
            return dummy
            
        return head
