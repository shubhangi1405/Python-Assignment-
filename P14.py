# Experiment 14: Stack with safe_pop()

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an item onto the top of the stack."""
        self._items.append(item)
        print(f'Pushed: {item}')

    def safe_pop(self):
        """Safely remove and return top element. Handles empty stack."""
        if self.is_empty():
            print('Stack is empty, nothing to pop.')
            return None
        item = self._items.pop()
        print(f'Popped: {item}')
        return item

    def peek(self):
        """View the top element without removing it."""
        if self.is_empty():
            print('Stack is empty.')
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def display(self):
        print(f'Stack (top -> bottom): {list(reversed(self._items))}')


# Main Program
s = Stack()

print('--- Pushing elements ---')
s.push(10)
s.push(20)
s.push(30)
s.display()

print(f'\nTop element (peek): {s.peek()}')
print(f'Stack size: {s.size()}')

print('\n--- Popping elements ---')
s.safe_pop()
s.safe_pop()
s.display()

print('\n--- Popping remaining + empty stack ---')
s.safe_pop()           # Pops last element
s.safe_pop()           # Stack now empty
s.safe_pop()           # Still empty
