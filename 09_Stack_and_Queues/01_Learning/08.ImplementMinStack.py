#https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        # The stack will store tuples: (val, min_val_at_this_point)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            # The new minimum is the smaller of the current value 
            # and the previous minimum at the top of the stack
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
