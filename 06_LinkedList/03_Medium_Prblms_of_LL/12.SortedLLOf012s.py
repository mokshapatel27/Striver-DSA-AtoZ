#https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        dummy0=Node(0)
        dummy1=Node(0)
        dummy2=Node(0)
        p0,p1,p2=dummy0,dummy1,dummy2
        
        curr=head
        while curr:
            if curr.data==0:
                    p0.next=curr
                    p0=p0.next
            elif curr.data==1:
                    p1.next=curr
                    p1=p1.next
            else:
                    p2.next=curr
                    p2=p2.next
                    
            curr=curr.next
                
        p0.next=dummy1.next if dummy1.next else dummy2.next
        p1.next=dummy2.next
        p2.next=None
            
        return dummy0.next
