#http://leetcode.com/problems/implement-stack-using-queues/description/

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    # Time Complexity: O(N)
    def push(self, x: int) -> None:
        self.queue.append(x)
        # Rotate the queue to bring the newly added element to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    # Time Complexity: O(1)
    def pop(self) -> int:
        return self.queue.popleft()

    # Time Complexity: O(1)
    def top(self) -> int:
        return self.queue[0]

    # Time Complexity: O(1)
    def empty(self) -> bool:
        return len(self.queue) == 0
