# Imports
from copy import deepcopy
    
class PriorityQueue:
    
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 10

    def __init__(self, max_size = DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty priority queue. This implementation
        use a max-heap data structure. The highest priority
        element is the maximum element.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Returns:
            a new PriorityQueue object (PriorityQueue)
        -------------------------------------------------------
        """        
        assert max_size > 0, "Heap size must be > 0"


        self._capacity = max_size
        self._values = [None] * self._capacity
        self._size = 0

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.isEmpty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        
        return self._size == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of elements in the priority queue.
        -------------------------------------------------------
        """
             
        return self._size
        
    def insert(self, element):
        """
        -------------------------------------------------------
        A copy of element is inserted into the priority queue.
        The element is placed at the last position and then it
        is percolated up to make sure the heap-order property 
        is maintained.                 
        Use: pq.insert(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert not self._size == self._capacity - 1, "Heap is Full"

        self._values [self._size] = deepcopy(element)
        i = self._size
        self._size += 1

        while i > 0:
            parent = (i - 1) // 2   

            if self._values[i] > self._values[parent]:
                temp = self._values[i]
                self._values[i] = self._values[parent]
                self._values[parent] = temp
                i = parent

            else:
                return
 
    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority element from the 
        priority queue. In this implementation the highest 
        priority element is the maximum element.
        Use: element = pq.remove()
        -------------------------------------------------------
        Returns:
            element - the highest priority element in the priority queue -
                the element is removed from the priority queue. (?)
        -------------------------------------------------------
        """
   
        assert self._size > 0, "Cannot remove from an empty priority queue"

        element = deepcopy(self._values[0])

        self._values[0] = self._values[self._size - 1]
        self._values[self._size - 1] = None
        self._size -= 1

        i = 0

        child = 2 * i + 1

        while child < self._size:
            if child != self._size - 1 and self._values[child] > self._values[child + 1]:
                child = child + 1

            if self._values [i] > self._values[child]:
                temp = self._values[i]
                self._values[i] = self._values[child]
                self._values[child] = temp

            i = child
            child = 2 * i + 1

        else:
            return element



    def peek(self):
        """
        -------------------------------------------------------
        returns the highest priority element of the priority 
        queue. In this implementation, the highest priority
        element is the maximum element
        Use: element = pq.peek()
        -------------------------------------------------------
        Returns:
            element - a copy of the highest priority element in 
            the priority queue -
                the element is not removed from the priority 
                queue. (?)
        -------------------------------------------------------
        """
        return self._values[0]
    
    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for element in pq:
        -------------------------------------------------------
        Returns:
            element - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for element in self._values:
            yield element

