#https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1

# Structure of linked list Node
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.top=None
        self.nsize=0

    def isEmpty(self):
        return self.top is None
        

    def push(self, x):
        newnode=Node(x)
        #Points the new node's next pointer to the current top node. This links the new node to the rest of the stack.
        newnode.next=self.top
        self.top=newnode
        self.nsize+=1
        

    def pop(self):
        if self.isEmpty():
            return -1
        #Saves the data of the current top node into a temporary variable
        popped=self.top.data
        self.top=self.top.next
        self.nsize-=1
        return popped


    def peek(self):
        if self.isEmpty():
            return -1
        return self.top.data


    def size(self):
        return self.nsize
