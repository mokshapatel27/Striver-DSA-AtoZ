#https://leetcode.com/problems/reverse-linked-list/submissions/2039518140/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
