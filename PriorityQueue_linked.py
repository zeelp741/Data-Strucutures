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
        self._next = None
        self._value = deepcopy(element)

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
        self._front = None
        self._rear = None
        self._count = 0 

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
        current = self._front
        previous = None
        while current is not None and current._value < element:
            previous = current
            current = current._next
        if current is None:
            # Reached end of Queue or Queue empty
            new_node = PQNode(element)
            if self._count == 0:
                self._rear = new_node
                self._front = new_node
            else:
                # Reached end of Queue
                self._rear._next = new_node
                self._rear = new_node
            self._count += 1
        else:
            # Somewhere in Queue
            new_node = PQNode(element)
            if previous is None:
                # Beginning of Queue
                self._front = new_node
            else:
                # Not beginning, update references
                previous._next = new_node
            self._count += 1
        return

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
        assert self._count > 0, "Cannot remove from an empty priority queue"
        element = self._front._value

        self._front = self._front._next

        self._count -= 1

        if self._count == 0:
            self._rear = None

        return deepcopy(element)

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
        assert self._count > 0, "Cannot peek at an empty priority queue"
        return deepcopy(self._front._value)


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


