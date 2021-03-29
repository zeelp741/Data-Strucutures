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
        # your code here

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
        # your code here

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
             
        # your code here
        
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
        # your code here
           
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
   
        # your code here

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
        # your code here
    
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
