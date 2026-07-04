#https://www.geeksforgeeks.org/problems/implement-queue-using-array/1

class myQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [0] * n
        self.front = 0
        self.rear = 0
        self.curr_size = 0

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.n

    def enqueue(self, x):
        if self.isFull():
            return
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.n
        self.curr_size += 1

    def dequeue(self):
        if self.isEmpty():
            return
        self.front = (self.front + 1) % self.n
        self.curr_size -= 1

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # rear points to the next empty slot, so the last element is at rear - 1
        return self.queue[(self.rear - 1 + self.n) % self.n]
