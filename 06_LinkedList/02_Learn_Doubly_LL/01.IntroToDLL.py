#https://www.geeksforgeeks.org/problems/create-a-doubly-linked-list-from-a-given-array/1

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
   def createDLL(self, arr):
        if not arr:
           return None
           
        head=Node(arr[0])
        curr=head 
         
        for i in range(1,len(arr)):
            new=Node(arr[i])
            curr.next=new
            new.prev=curr
            curr=new
        return head
         
