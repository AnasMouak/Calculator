#!/usr/bin/python3

class Stack:
    """
    This class implements a stack data structure.
    """
    def __init__(self):
        """
        Initializes a new instance of the Stack class.
        """
        self.items = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Returns:
            The item removed from the top of the stack, or None if the stack
            is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack, or None if the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            The number of items in the stack.
        """
        return len(self.items)
