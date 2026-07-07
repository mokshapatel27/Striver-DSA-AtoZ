#https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1

# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
        

    def isEmpty(self):
        return self.front is None
        

    def enqueue(self, x):
        # Add element x to the rear
        newnode=Node(x)
        if self.isEmpty():
            self.front=self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
        self.count+=1
        

    def dequeue(self):
        if self.isEmpty():
            return
        
        # Move front forward
        self.front = self.front.next
        self.count -= 1
        
        # If queue becomes empty, reset rear as well
        if self.front is None:
            self.rear = None

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.front.data

    def size(self):
        return self.count
