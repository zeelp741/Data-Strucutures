"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Zeel Patel
ID:     200881210
Email:  pate1210@mylaurier.ca
__updated__ = '2021-02-03'
------------------------------------------------------------------------
"""

# pylint: disable=W0212

from copy import deepcopy

class Stack:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_SIZE = 10

    def __init__(self, max_size = DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a 
        fixed-size Python list.
        
        Use: stack = Stack(max_size)
        Use: stack = Stack()    # uses default max size
        -------------------------------------------------------
        Parameters:
            max_size - maximum size of the Stack (int > 0)
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        
        assert max_size > 0, "Queue size must be > 0"
 
        self._capacity = max_size
        self._values = [None] * self._capacity
        self._top = -1

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        
        return self._top == -1
        
#         empty = False

#         if self._values[0] == None:
#             empty = True     
#         
#         return empty


    
    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the stack is full.
        Use: b = stack.isFull()
        -------------------------------------------------------
        Returns:
            True if stack is full, False otherwise
        -------------------------------------------------------
        """
        
#         full = True
#         
#         if self._top != None:
#             full = False
#         return full

        status = False
        if self._top == self._capacity:
            status = True
        
        return status


    def push(self, element):
        """
        -------------------------------------------------------
        Pushes a copy of the given element onto the top of the 
        stack.
        Use: stack.push(element)
        -------------------------------------------------------
        Parameters:
            element - the data element to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert not self.isFull(), "Stack is full"
        
        self._top += 1
        self._values[ self._top ] = deepcopy( element )
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The data element is 
        removed from the stack. Attempting to pop from an empty 
        stack throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """

        value = deepcopy(self._values[ self._top ])
        self._top -=1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack without
        removing it.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        

        element = deepcopy(self._values[self._top])
        return element

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        #your code goes here

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        

    
        alternating = 0
        size = 0
    
        while(self._values[-1] == None):
            if alternating % 2 == 0:
                if source1._top == -1:
                    break
                self.push(source1._values[source1._top])
                source1._top -= 1
                size += 1
            elif alternating % 2 == 1:
                if source2._top == -1:
                    break
                self.push(source2._values[source2._top])  
                source2._top -= 1    
                size += 1  

            alternating += 1
                    
        while (size <= self.DEFAULT_SIZE):

            size += 1
            
            if source1._top == -1:
                self.push(source2._values[source2._top])
                source2._top -= 1
                size += 1

            elif(source2._top == -1):
                self.push(source1._values[source1._top])
                source1._top -= 1
                size += 1

                
        

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into two separate target stacks 
        with values alternating into the targets. At finish 
        source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
    
    
        alternating = 0
        while(self._top != -1):
            alternating += 1
            if alternating % 2 == 0:
                target2.push(self._values[self._top])
            elif (alternating % 2 == 1):
                target1.push(self._values[self._top])
            self._top -= 1
            
        return target1, target2       

            
        

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for value in stack:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
