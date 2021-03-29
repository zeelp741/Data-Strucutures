# Imports
from copy import deepcopy

class PriorityQueue:

    DEFAULT_SIZE = 60
    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
                    
        assert max_size > 0, "List size must be > 0"
        self._capacity = max_size
        self._values = [None] * self._capacity
        self._count = 0
        self._first = None
                

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
        #your code here
    
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
        #your code here

    def insert(self, element):
        """
        -------------------------------------------------------
        A copy of element is appended to the end of the the 
        Python list storing the data in the Priority Queue, and
        _first is updated as appropriate to the index of
        element with the highest priority.
        Use: pq.insert(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        #your code here
                      

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the element of _first.
        _first is the index of the element with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        #your code here

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority element from the priority queue.
        Use: element = pq.remove()
        -------------------------------------------------------
        Returns:
            element - the highest priority element in the priority queue -
                the element is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        #your code here

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority element of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            element - a copy of the highest priority element in the priority queue -
                the element is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        #your code here


    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
