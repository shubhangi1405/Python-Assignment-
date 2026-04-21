# Experiment 15: Queue using collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._items.append(item)
        print(f'Enqueued: {item}')

    def safe_dequeue(self):
        """Safely remove and return front element. Handles empty queue."""
        if self.is_empty():
            print('Queue is empty, cannot dequeue.')
            return None
        item = self._items.popleft()
        print(f'Dequeued: {item}')
        return item

    def front(self):
        """Peek at the front element without removing."""
        if self.is_empty():
            print('Queue is empty.')
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def display(self):
        print(f'Queue (front -> rear): {list(self._items)}')


# Main Program
q = Queue()

print('--- Enqueueing elements ---')
q.enqueue('Task A')
q.enqueue('Task B')
q.enqueue('Task C')
q.enqueue('Task D')
q.display()

print(f'\nFront element: {q.front()}')
print(f'Queue size   : {q.size()}')

print('\n--- Dequeueing elements ---')
q.safe_dequeue()
q.safe_dequeue()
q.display()

print('\n--- Dequeueing remaining + empty queue ---')
q.safe_dequeue()
q.safe_dequeue()
q.safe_dequeue()  # Empty queue
q.safe_dequeue()  # Still empty
