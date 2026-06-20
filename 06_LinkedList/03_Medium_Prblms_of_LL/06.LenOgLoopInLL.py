#https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow,fast=head,head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                count=1
                curr=slow
                
                while curr.next!=slow:
                    count+=1
                    curr=curr.next
                return count
        return 0
