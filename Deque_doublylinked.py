

# Imports
from copy import deepcopy



class DNode:

    def __init__(self, element):
        """
        -------------------------------------------------------
        Initializes a Deque node.
        Use: node = DNode(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            _data - data value for node (?)
            _prev - pointer to another Deque node (DNode)
            _next - pointer to another Deque node (DNode)
        Returns:
            a new DNode object (DNode)
        -------------------------------------------------------
        """
        self._data = deepcopy(element)
        self._prev = None
        self._next = None

class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Deque.
        Use: deque = Deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the Deque is empty.
        Use: b = deque.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of data elements in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def insertFront(self, element):
        """
        -------------------------------------------------------
        Inserts a copy of the data element into the front of the
        Deque.
        Use: deque.insertFront(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = DNode(deepcopy(element))
        current = self._front
        
        if self.isEmpty():
            self._rear = node
            
        self._front = node
        self._front._next = current
        self._count += 1
        
        return

    def insertEnd(self, element):
        """
        -------------------------------------------------------
        Inserts a copy of the given element into the rear of 
        the Deque.
        Use: deque.insertEnd(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = DNode(deepcopy(element))
        if self.isEmpty():
            self._front = node
        self._rear._next = node
        self._rear = node 
        self._count += 1
        return

    def removeFront(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.removeFront()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        
        assert self._front is not None
        
        value = self._front._data
        self._front = self._front._next
        
        if self._front == None:
            self._front._prev = None
        self._count -= 1
        
        if self.isEmpty():
            self._front = None
            self._rear = None
        
        return deepcopy(value)
        
    def removeEnd(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.removeEnd()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None
        
        value = self._rear._data
        self._rear = self._rear._prev
        
        if self._rear != None:
            self._rear._next= None
        self._count -= 1
        
        if self.isEmpty():
            self._front = None
            self._rear = None
        return deepcopy(value)

    def peekFront(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peekFront()
        -------------------------------------------------------
        Returns:
            a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """

        assert self._front is not None
        
        value = self._front._data
        
        return deepcopy(value)
    
    
    def peekEnd(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peekEnd()
        -------------------------------------------------------
        Returns:
            a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        
        assert self._rear is not None
        
        value = self._rear._data
        
        return deepcopy(value)


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in deque.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        
        #your code goes here


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in deque.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            a copy of the minimum value in source (?)
        -------------------------------------------------------
        """

        #your code goes here


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._data
            current = current._next
