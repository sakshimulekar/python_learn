# 5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"

class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        # Push the element to the enqueue stack
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack:
            # If the dequeue stack is empty, transfer elements from enqueue stack to dequeue stack
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        if not self.dequeue_stack:
            # If both stacks are empty, return None
            return None

        # Pop and return the front element from the dequeue stack
        return self.dequeue_stack.pop()

# Test the queue
queue = QueueUsingStack()
print(queue.dequeue())  # Output: None

queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1

queue.enqueue(3)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: None
