# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        # Move all elements from q1 to q2
        while not self.q1.empty():
            self.q2.put(self.q1.get())

        # Push the new element into q1
        self.q1.put(value)

        # Move back all elements from q2 to q1
        while not self.q2.empty():
            self.q1.put(self.q2.get())

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()

# Test the stack
stack = StackUsingQueue()
print(stack.pop())  # Output: None

stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1
print(stack.pop())  # Output: None
