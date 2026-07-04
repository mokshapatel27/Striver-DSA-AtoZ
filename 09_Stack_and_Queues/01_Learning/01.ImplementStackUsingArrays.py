#https://www.geeksforgeeks.org/problems/implement-stack-using-array/1

class myStack:
    def __init__(self, n):
        self.size=n
        #list with same element n times
        self.stack=[-1]*n
        #pointer for top element -1 denotes it is completely empty at strt
        self.top=-1

    
    def isEmpty(self):
        return self.top== -1

    
    def isFull(self):
        #this means the top ptr as reached final idx size-1
        return self.top==self.size-1

    
    def push(self, x):
        if not self.isFull():
            self.top+=1
            #places x at where self.top points
            self.stack[self.top]=x

    
    def pop(self):
        if not self.isEmpty():
            self.top-=1

    
    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[self.top]
        
