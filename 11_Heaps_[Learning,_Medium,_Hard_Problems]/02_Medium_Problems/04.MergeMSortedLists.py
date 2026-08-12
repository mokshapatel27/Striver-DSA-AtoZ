#https://leetcode.com/problems/merge-k-sorted-lists/description/

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Push the head of each non-empty list into the min-heap
        # Include list index 'i' to avoid direct comparison between ListNode objects
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        # Pop the smallest element and push its next node if present
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
