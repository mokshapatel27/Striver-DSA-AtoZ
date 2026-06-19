#https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        curr=head
        
        while curr:
            if curr.data==key:
                return True
                
            curr=curr.next
            
        return False
