#https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # Handle empty list or single node
        if not head or not head.next:
            return []
            
        # Step 1: Find the tail of the doubly linked list
        tail = head
        while tail.next:
            tail = tail.next
            
        pairs = []
        
        # Step 2: Use two pointers to find pairs with the target sum
        # The loop breaks when pointers cross or point to the same node
        while head != tail and tail.next != head:
            current_sum = head.data + tail.data
            
            if current_sum == target:
                pairs.append([head.data, tail.data])
                head = head.next
                tail = tail.prev
            elif current_sum < target:
                head = head.next  # Look for a larger value
            else:
                tail = tail.prev  # Look for a smaller value
                
        return pairs
