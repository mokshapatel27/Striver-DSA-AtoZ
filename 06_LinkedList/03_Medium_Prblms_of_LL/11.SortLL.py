#https://leetcode.com/problems/sort-list/  

#LEFT!!

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head
        
        # 1. Split the list in half using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid, slow.next = slow.next, None  # Break the list
        
        # 2. Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 3. Merge inline using a dummy node
        dummy = tail = ListNode(0)
        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
            
        tail.next = left or right
        return dummy.next
