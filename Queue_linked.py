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

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

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
        assert self._front is not None, "Cannot remove from an empty queue"

        value = self._front._data
        self._front = self._front._next
        self._count -= 1

        if self._front is None:
            self._rear = None
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
        assert self._front is not None, "Cannot peek at an empty queue"

        return deepcopy(self._front._data)

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source Queues (source1 and source2) into 
        the current (self) Queue.
        When finished, the contents of source1 and source2 are
        interlaced into self Queue and source1 and source2 are
        empty.
        (iterative algorithm)
        Use: queue.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1.isEmpty() == False and source2.isEmpty() == False:
            self.enqueue(source1.dequeue())
            self.enqueue(source2.dequeue())
            
        while source1.isEmpty() == False:
            self.enqueue(source1.dequeue)
            
        while source2.isEmpty() == False:
            self.enqueue(source2.dequeue)
            
        return        

    def split(self):
        """
        -------------------------------------------------------
        Splits the current Queue into two parts. target1 contains the
        first half, target2 the second half. The self Queue (current
        Queue) becomes empty.
        Use: target1, target2 = queue.split()
        -------------------------------------------------------
        Returns:
            target1 - a new Queue with >= 50% of the original Queue (Queue)
            target2 - a new Queue with <= 50% of the original Queue (Queue)
        -------------------------------------------------------
        """
        
        target1 = Queue()
        target2 = Queue()
        
        if self._count % 2 == 1:
            midpoint = (self._count // 2) + 1
        else:
            midpoint = (self._count // 2)
        
        for i in range(midpoint):
            target1.enqueue(self.dequeue())
            
        while self.isEmpty() == False:
            target2.enqueue(self.dequeue())
            
        return target1, target2
        
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the queue into separate target queues with values
        alternating into the targets. At finish queue is empty.
        (iterative algorithm)
        Use: target1, target2 = queue.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from queue (Queue)
            target2 - contains remaining values from queue (Queue)
        -------------------------------------------------------
        """
        
        target1 = Queue()
        target2 = Queue()
        counter = 0
        
        while self.isEmpty() == False:
            if counter % 2 == 0:
                target1.enqueue(self.dequeue())
            else:
                target2.enqueue(self.dequeue())   
            counter += 1
        return target1, target2
                
    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether the current Queue is identical to target
        queue. Values of current Queue and target are compared and if all 
        contents are identical and in the same order, returns True,
        otherwise returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = queue.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if queue and target are identical, False
                otherwise. (boolean)
        -------------------------------------------------------
        """
        
        current_self = self._front
        current_target = target._front
        counter = 0
        identical = False
 
        while current_self is not None and current_target is not None:
            
            if current_self._data == current_target._data:
                counter += 1
            
            current_self = current_self._next
            current_target = current_target._next
            
        if counter == self._count:
            identical = True

        return identical

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
        current = self._front

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
        current = self._front
 
        while current is not None:
            print(current._data)
            current = current._next
        return

