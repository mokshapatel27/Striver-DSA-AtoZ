#https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

'''LOGIC:
slow moves one step at a time.
fast moves two steps at a time.

By the time fast reaches the end of the list, slow will be exactly at the middle node. This handles both odd and even-lengthed lists perfectly without needing to calculate the total length first.'''
