# Imports
from copy import deepcopy


class PriorityQueue:

    DEFAULT_SIZE = 10
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
        
        return self._count == 0

    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is full.
        Use: b = pq.isFull()
        -------------------------------------------------------
        Returns:
            True if priority queue is full, False otherwise.
        -------------------------------------------------------
        """
        
        return self._count ==  self._capacity
    
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
        return self._count

    def size(self):
        """
        -------------------------------------------------------
        Returns the size of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of elements in the priority queue.
        -------------------------------------------------------
        """
        return self._count

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
        assert self._count < self._capacity, "Not enough space"

        
        if self._first is None:
            self._first = 0
        elif element < self._values[self._first]:
            self._first = self._count

        self._values[self._count] = deepcopy(element)
        self._count += 1
        return None                

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

        if self._count == 1:
            self._first = 0

        elif self._count == 0:
            self._first = None

        else:
            self._first = 0
            for x in range(len(self._values)):
                if self._values[x] < self._values[self._first]:
                    self._first = x

        return

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

        assert not self._count == 0, "Queue is Empty"
        
        element = deepcopy(self._values[self._first])
        if self._first != self._count -1:

            for i in range(self._first, self._count - 1):
                self._values[i] = self._values[i+1]

            self._values[ self._count - 1] = None
            self._count -= 1
        else:
            self._values[self._first] = None
            self._count -= 1
        
        index = 0
        if self._count != 0:
            temp = self._values[0]

            for i in range(self._count):
                if self._values[i] < temp:
                    temp = self._values[i]
                    index = i

        else:

            index = None
        self._first = index
        return element

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
        assert self.isEmpty() == 0, "Cannot peek at an empty priority queue"
        value = deepcopy(self._values[self._first])
        return value

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a Priority Queue into two depending on an external
        key. The current Priority Queue (pq) will be empty when the 
        method ends. The elements smaller than than key 
        go into target1 and the elements larger than key go into
        target2. The order of the elements from current 
        Priority Queue (pq) is preserved.
        Use: target1, target2 = pq.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            target1 - a Priority Queue that contains all element
                with priority higher than key (PriorityQueue)
            target2 - a Priority Queue that contains all elements with
                priority lower than or equal to key (PriorityQueue)
        -------------------------------------------------------
        """
        target1 = PriorityQueue()
        target2 = PriorityQueue()

        if self._count != 0 :
            
            for value in self._values:

                if value < key:  # Higher priority
                    target1.insert(deepcopy(value))
                else:
                    target2.insert(deepcopy(value))

            for value in self._values:
                self.remove()
            
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a Priority Queue into two with elements going to
        alternating Priority Queues. The elements smaller than 
        than key go into target1 and the elements larger than 
        key go into target2. The current Priority Queue
        is empty when the method ends. The order of the elements
        in current Priority Queue is preserved.
        Use: target1, target2 = pq.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a Priority Queue that contains alternating 
                elements from the current Priority Queue (Priority_Queue)
            target2 - a Priority Queue that contains alternating 
                elements from the current Priority Queue (Priority_Queue)
        -------------------------------------------------------
        """

        target1 = PriorityQueue()
        target2 = PriorityQueue()

        if self._count != 0:
            counter = 0

            for value in self._values:
                if counter % 2 == 0:
                    target1.insert(deepcopy(value))

                else:
                    target2.insert(deepcopy(value))

                counter += 1

            for value in self._values:
                self.remove()

        return target1, target2


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
