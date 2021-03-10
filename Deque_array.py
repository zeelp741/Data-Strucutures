from copy import deepcopy

class Deque:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 10
    
    def __init__(self, max_size = DEFAULT_SIZE):
        
        assert max_size > 0, "Queue size must be > 0"
        
        self._capacity = max_size
        self._values = [None] * self._capacity
        self._front = 1
        self._rear = 0
        self._top = -1
        self._count = 0
    
    def insertFront(self, element):
        """
        -------------------------------------------------------
        Inserts element to the front of the stack
        Use: stack.insertFront(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = (self._front - 1) % self._capacity
        self._values[self._front] = deepcopy(element)
        self._count += 1
        return
        
    def insertEnd(self, element):
        """
        ---------------------------------------------------------
        Adds a copy of data element to the end of the List.
        Use: lst.insertEnd(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._rear = (self._rear + 1) % self._capacity
        self._values[self._rear] = deepcopy(element)
        self._count += 1
        return
        
    def removeFront(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = queue.dequeue()
        -------------------------------------------------------
        Returns:
            element - the data element at the front of the queue is 
            returned, the data element is removed from the queue (?)
        -------------------------------------------------------
        """
        assert not self.isEmpty(), "Cannot remove from an empty queue"
        value = self._values[self._front]
        self._values[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._count -= 1
        return value
    
    def removeEnd(self):
        """
        -------------------------------------------------------
        removes the data element from the rear of Deque and returns it
        Use: value = deque.removeEnd()
        -------------------------------------------------------
        Returns:
            value - the value at the top of deque (?)
        -------------------------------------------------------
        """
        assert not self.isEmpty(), "Cannot remove from an empty queue"
        value = self._values[self._rear]
        self._values[self._rear] = None
        self._rear = (self._rear + 1) % self._capacity
        self._count -= 1
        return value
        
    def size(self):
        """
        -------------------------------------------------------
        Returns the number of data elements in the List.
        Use: n = len.size()
        -------------------------------------------------------
        Returns:
            the number of data elements in the List.
        -------------------------------------------------------
        """
        return self._count
    
    def peekFront(self):
        """
        -------------------------------------------------------
        returns the value at the front of queue without removing it
        Use: v = queue.front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[self._front])
        return value
        
    def peekEnd(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack without
        removing it.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        element = deepcopy(self._values[self._top])
        return element
        
    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = queue.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0
        
    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = queue.isFull()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        return self._count == self._capacity

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for value in stack:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        j = self._front
        i = 0

        while i < self._count:
            yield self._values[j]
            i += 1
            j = (j + 1) % self._capacity
    
    
    
    
    
    
        
        
