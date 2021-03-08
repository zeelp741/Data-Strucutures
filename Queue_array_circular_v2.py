from copy import deepcopy

class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 10

    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size 
        Python list.
        Use: queue = Queue(max_size)
        Use: queue = Queue()  # uses default max size
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert max_size > 0, "Queue size must be > 0"

        self._capacity = max_size
        self._values = [None] * self._capacity
        self._front = -1
        self._rear = -1

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
        
        if self._front == None:
            return True
        else:
            return False
        
    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        
        return self._rear > self._capacity - 1

    def size(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of data elements in the queue.
        -------------------------------------------------------
        """
        if self.isEmpty():
            return 0
        else:
            return self._rear - self._front + 1

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of data elements in the queue.
        -------------------------------------------------------
        """
        if self.isEmpty():
            return 0
        else:
            return self._rear - self._front + 1
        
    def enqueue(self, element):
        """
        -------------------------------------------------------
        Adds a copy of the element to the rear of the queue.
        Use: queue.enqueue( element )
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        assert not self.isFull(), "Queue is full"
 
        self._values[self._rear] = deepcopy(element)
        self._rear += 1
        return

    def dequeue(self):
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
 
        value = deepcopy( self._values[ self._front ] )
        self._front = self._front + 1
 
        if self._front == self._rear : #Queue becomes empty
            self._front = -1
            self._rear = -1
 
        return value    

    def peek(self):
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
        
        value = deepcopy(self._front)
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        j = self._front
        count = self.size()
        i = 0

        while i < count:
            yield self._values[j]
            i += 1
            j = (j + 1) % self._capacity
            
    def print(self):
        """
        -------------------------------------------------------
        Prints the contents of List from beginning to end.
            Use: lst.print()
        -------------------------------------------------------
        Returns:
            one
        -------------------------------------------------------
        """
        current = self._rear
 
        while current is not None:
            print(current._data)
            current = current._next
        return
