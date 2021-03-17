"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Zeel Patel
ID:     200881210
Email:  pate1210@mylaurier.ca
__updated__ = '2021-03-03'
------------------------------------------------------------------------
"""

from copy import deepcopy


class Node:

    def __init__(self, element):
        """
        -------------------------------------------------------
        Initializes a linked-list node that contains a copy of 
        the given element and a link pointing to None.
        Use: node = Node(element)
        -------------------------------------------------------
        Parameters:
            element - data value for node (?)
        Returns:
            a new Node object (Node)
        -------------------------------------------------------
        """
        self._data = deepcopy(element)
        self._next = None


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Queue. The data elements are stored
        in a linked-list data structure.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """

        self._front = None
        self._rear = None
        self._count = 0

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the Queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        
        return self._count == 0
    
    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """

        return False

    def size(self):
        """
        -------------------------------------------------------
        Returns the number of elements in the queue.
        Use: n = queue.size()
        -------------------------------------------------------
        Returns:
            the number of data elements in the queue.
        -------------------------------------------------------
        """
    
        return self._count
    
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of data elements in the queue.
        -------------------------------------------------------
        """

        return self._count

    def enqueue(self, element):
        """
        -------------------------------------------------------
        Adds a copy of the given element to the rear of queue.
        Use: queue.enqueue(value)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None 
        -------------------------------------------------------
        """
        node = Node(deepcopy(element))
        
        if self.isEmpty():
            self._front = node
        else:
            node._next = self._rear
        self._rear = node
        self._count += 1
        return
        
    def dequeue(self):
        """
        -------------------------------------------------------
        Removes and returns the value at the front of the queue.
        Use: value = queue.dequeue()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        assert not self._count == 0 , "Queue is empty"
        
        value = deepcopy(self._front._data)
        
        if self._count == 1:
            self._front = None
            self._rear = None
        else:
            current = self._rear
            while current._next._next != None:
                current = current._next
            self._front = current
            self._front._next = None
        self._count -= 1
        return value
            
    def peek(self):
        """
        -------------------------------------------------------
        returns a copy of the data element at the front of queue
        without removing it.
        Attempting to peek at an empty queue throws an exception.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None 
        
        current = self._front
        value = deepcopy(current._data)
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._rear

        while current is not None:
            yield current._data
            current = current._next
            
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

