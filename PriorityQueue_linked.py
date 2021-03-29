"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown and Masoomeh Rudafshani
ID:      999999999 and 123456789
Email:   dbrown@wlu.ca and mrudafshani@wlu.ca
Section: CP164 OC
__updated__ = "2021-01-20"
-------------------------------------------------------
"""

# Imports
from copy import deepcopy


class PQNode:

    def __init__(self, element):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of 
        the given element and a link pointing to None.
        Use: node = PQNode(element)
        -------------------------------------------------------
        Parameters:
            element - data element for node (?)            
        Returns:
            a new PriorityQueue object (PQNode)
        -------------------------------------------------------
        """
        #your code here

class PriorityQueue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Returns:
            a new PriorityQueue object (PriorityQueue)
        -------------------------------------------------------
        """
        #your code here

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
        A copy of element is inserted into the priority queue.
        Elements are stored in priority order. The minimum element
        has the highest priority.
        Use: pq.insert(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        #your code here

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority element from the
        priority queue.
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
            a copy of the highest priority element in the priority queue -
                the element is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        #your code here


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next
