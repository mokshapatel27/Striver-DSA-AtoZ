#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next ==None :
            return None
        index = 0
        node = head
        while node != None:
            index += 1
            node = node.next
        n = index
        half = n // 2 - 1
        node = head
        for i in range(half):
            node = node.next
        node.next = node.next.next
        return head
