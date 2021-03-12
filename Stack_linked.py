"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Zeel Patel
ID:     200881210
Email:  pate1210@mylaurier.ca
__updated__ = DATE
------------------------------------------------------------------------
"""
# pylint: disable=W0212

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

class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. The data elements are stored
        in a linked-list data structure.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._top = None
        self._count = 0

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.isEmpty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return self._top is None

    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the Stack is full.
        Use: b = stack.isFull()
        -------------------------------------------------------
        Returns:
            True if stack is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the Stack.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in stack.
        -------------------------------------------------------
        """
        return self._count

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the data element at the top of Stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the data element at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot peek at an empty stack"
        value = deepcopy(self._top._data)
        return value

    def push(self, element):
        """
        -------------------------------------------------------
        Pushes a copy of the given element onto the top of stack.
        Use: stack.push(element)
        -------------------------------------------------------
        Parameters:
            element - the data element to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        newNode = Node(deepcopy(element))
        newNode._next = self._top
        self._top = newNode
        self._count += 1
        return


    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of the stack. The data element
        is removed from the stack. Attempting to pop from an
        empty stack throws an exception.
        Use: element = stack.pop()
        -------------------------------------------------------
        Returns:
            element - the data element at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot pop from an empty stack"

        element = self._top._data
        self._top = self._top._next
        self._count -= 1
        return element

    def _move_top_to_top(self, source):
        """
        -------------------------------------------------------
        Moves the top node from the source stack to the self stack.
        The self stack will the old top node of the source stack.
        The source stack top is updated. Equivalent of
        self.push(source.pop()), but moves nodes, not data.
        Use: target._move_top_to_top(source)
        -------------------------------------------------------
        Parameters:
            source - a linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._top is not None, "Cannot move the top of an empty stack"

        temp = source._top
        source._top = source._top._next
        temp._next = self._top
        self._top = temp
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        #your code goes here

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source Stacks (source1 and source2) into 
        the current (self) Stack.
        When finished, the contents of source1 and source2 are 
        interlaced into current Stack and source1 and source2 are
        empty.
        Use: stack.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked stack (Stack)
            source2 - an linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        
        while source1.isEmpty() == False and source2.isEmpty() == False:
            self._move_top_to_top(source1)
            self._move_top_to_top(source2)
            
        while source1.isEmpty() == False:
            self._move_top_to_top(source1)
            
        while source2.isEmpty() == False:
            self._move_top_to_top(source2)
    
    def split(self):
        """
        -------------------------------------------------------
        Splits the current Stack into two parts. target1 contains the
        first half, target2 the second half. The self Stack (current
        List) becomes empty.
        Use: target1, target2 = stack.split()
        -------------------------------------------------------
        Returns:
            target1 - a new Stack with >= 50% of the original Stack (Stack)
            target2 - a new Stack with <= 50% of the original Stack (Stack)
        -------------------------------------------------------
        """
        
        target1 = Stack()
        target2 = Stack()
                
        if self._count % 2 == 1:
            midpoint = (self._count // 2) + 1
        else:
            midpoint = (self._count // 2)
        
        for i in range(midpoint):
            target1._move_top_to_top(self)
            
        while self.isEmpty() == False:
            target2._move_top_to_top(self)
            
        return target1, target2
            
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the current Stack into separate target Stacks with 
        values alternating into the targets. At finish the current
        Stack is empty.
        Use: target1, target2 = stack.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        counter = 0
        
        while self.isEmpty() == False:
            if counter % 2 == 0:
                target2._move_top_to_top(self)
            else:
                target1._move_top_to_top(self)
                
            counter += 1
            
        return target1, target2
             

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from top to bottom.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            _data - the next value in source (?)
        -------------------------------------------------------
        """
        current = self._top

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
        current = self._top
 
        while current is not None:
            print(current._data)
            current = current._next
        return

