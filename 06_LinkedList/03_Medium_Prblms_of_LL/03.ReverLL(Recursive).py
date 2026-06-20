#https://leetcode.com/problems/reverse-linked-list/description/

#recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node, it's already reversed
        if not head or not head.next:
            return head

        newh=self.reverseList(head.next)

        head.next.next=head
        head.next=None
        return newh 
