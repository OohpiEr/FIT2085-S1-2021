class Stack:
    def __init__(self, capacity):
        """Builds a stack with given capacity > 0."""
        if capacity <= 0:
            raise Exception("The capacity must be positive")
        self.the_array = [None] * capacity
        self.top = -1 # the index of the top element
    
    def size(self):
        """Returns the size, i.e. the number
        of elements in the container."""
        return self.top+1
    
    def is_empty(self):
        """Returns True if and only if the container is empty."""
        return self.size()==0
        
    def is_full(self):
        """Returns True if and only if the container is full."""
        return self.size() >= len(self.the_array)
         
    def push(self, item):
        """Places the given item at the top of the stack
        if there is capacity, or raises an Exception."""
        if self.is_full():
          raise Exception("Stack is full.")
        self.top += 1
        self.the_array[self.top] = item
        ## ALT: If we had started with top=-1, we could instead use:
        ## self.the_array[self.top+1] = item
        ## self.top += 1
        
    def pop(self):
        """Removes and returns the top element of the stack,
        or raises an Exception if there is none."""
        if self.is_empty():
          raise Exception("Tried to pop from an empty stack.")
        element = self.the_array[self.top]
        self.top -= 1
        return element
      
    def peek(self):
      """Returns the value on the top of the stack. Raises an
      IndexError if the stack is empty."""
      if self.is_empty():
        raise IndexError("Attempted to peek an empty stack.")
      return self.the_array[self.top]
    
    def reset(self):
        """Removes all elements from the container."""
        self.top = -1
