#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.instk=[]
        self.outstk=[]

    def push(self, x: int) -> None:
        self.instk.append(x)

    def pop(self) -> int:
        self.peek()
        return self.outstk.pop()

    def peek(self) -> int:
        # If out_stk is empty, move all elements from in_stk to out_stk
        if not self.outstk:
            while self.instk:
                self.outstk.append(self.instk.pop())
        return self.outstk[-1]

    def empty(self) -> bool:
        return not  self.instk and not self.outstk
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
