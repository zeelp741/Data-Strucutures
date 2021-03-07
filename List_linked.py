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

class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty List.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._head = None
        self._tail = None
        self._count = 0

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the List is empty, False otherwise.
        -------------------------------------------------------
        """
        
        #your code goes here


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of elements in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count


    def prepend(self, element):
        """
        -------------------------------------------------------
        Adds a copy of the given element to the head of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            element - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = Node(element)
        if self._count == 0:
            self._tail = node
        else:
            node._next = self._head
        self._head = node
        self._count += 1
    
        return

    def append(self, element):
        """
        ---------------------------------------------------------
        Adds a copy of element to the end of the List.
        Use: lst.append(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        node = Node(element)
        
        if self._count == 0:
            self._head = node
        else:                 
            self._tail._next = node 
        self._tail = node 
        self._count +=1 
        
        return


    def insert(self, i, element):
        """
        -------------------------------------------------------
        A copy of the given element is added to index i.
        If i outside of range of -len(List) to len(List) - 1, the 
        data element is prepended or appended as appropriate.
        Use: lst.insert(i, element)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
            # Create the new node.
        if i == 0 or i < -self._count :                     # Add value to the head of the List                        
            self.prepend(element)
        elif i == self._count:          # Add value to the end of the List
            self.append(element)
        elif self.isEmpty():
            self.append(element)
        elif i > self._count:
            self.append(element)
                                
        else:
            
            if i < 0:
                i = self._count + i    
            
            node = Node(element)                    # Add in the middle of the List - not to head or tail
            counter = 0
            
            current = self._head
            previous = None
            
            while counter != i:
                previous = current
                current = current._next
                counter += 1
                
            previous._next = node
            node._next = current
 
            self._count += 1
        return

    def _linear_search(self, element):
        """
        -------------------------------------------------------
        Searches for the first occurrence of the given element
        in the List.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            previous - pointer to the node previous to the node containing the given element (Node)
            current - pointer to the node containing the given element (Node)
            index - index of the node containing the given element (int)
        -------------------------------------------------------
        """
        current = self._head
        previous = None
        index = 0
        
        while current is not None and current._data != element:
            previous = current
            current = current._next
            index += 1
            
        if current is None:
            index = -1
            
        return previous, current, index
 
    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        max_data = -99999999
        current = self._head
        
        while current != None:
            if current._data > max_data:
                max_data = current._data
            
            current = current._next
            
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        
        min_data = 99999999
        current = self._head
        
        while current != None:
            if min_data > current._data:
                min_data = current._data
                
            current = current._next
            
        return min_data

    def count(self, element):
        """
        -------------------------------------------------------
        Finds the number of times the given element appears in 
        the List.
        Use: n = lst.count(element)
        -------------------------------------------------------
        Parameters:
            element - a partial data element (?)
        Returns:
            number - number of times element appears in List (int)
        -------------------------------------------------------
        """
        
        number = 0
        current = self._head
    
        while current is not None:
            if current._data == element:
                number += 1

            current = current._next
        return number

    def remove(self, element):
        """
        -------------------------------------------------------
        Finds and removes the first data element in list that 
        matches the given element.
        Use: b = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            b - True if remove is successful, False otherwise
        -------------------------------------------------------
        """
        
        state = False
        
        previous, current, index = self._linear_search(element)
        if index >= 0:

            if previous is None:
                self._head = current._next
            else:
                previous._next = current._next
            if current._next is None:
                self._tail = previous
            self._count -= 1
            state = True
        return state
        
    
    def find(self, element):
        """
        -------------------------------------------------------
        Finds the first element in the List that matches 
        the given element.
        Use: b = lst.find(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            b - True if the value is found, False otherwise
        -------------------------------------------------------
        """
        
        _, current, _ = self._linear_search(element)

        if current is not None:
            b = True
        else:
            b = False
        return b
        
    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        
        current = self._head
        
        value = current._data
        
        return value

    def indexOf(self, element):
        """
        -------------------------------------------------------
        Finds location of the given data element in the List.
        Use: n = lst.indexOf(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            i - the index of the location of element in the List,
                 -1 if the element is not in the list.
        -------------------------------------------------------
        """

        current = self._head
        index = 0
        counter = 0
        found = False
        
        while current != None:
            if current._data == element:
                index = counter
                found = True
                
            counter += 1
            current = current._next
            
        if not found:
            index = -1
            
        return index
                

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        #your code goes here


    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        current = self._head
        
        if i < 0:
            i = self._count + i
        
        j = 0

        while j < i:
            current = current._next
            j += 1

        value = deepcopy(current._data)
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        current = self._head
        
        if i < 0:
            i = self._count + i
        
        j = 0

        while j < i:
            current = current._next
            j += 1

        current._data = deepcopy(value)
        return value

    def __contains__(self, element):
        """
        ---------------------------------------------------------
        Determines if the list contains the element.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        current = self._head
        found = False
        
        
        while current != None:
            if current._data == element:
                found = True
            current = current._next
            
        return found
     
    def remove_head(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_head()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        current = self._head
        if self._count != 0:
            value = current._data
            self.remove(value)
        else:
            value = -1
        return value
 
    def remove_many(self, element):
        """
        -------------------------------------------------------
        Finds and removes all data element in the list that match
        the given element.
        Use: lst.remove_many(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        current = self._head
        
        while current != None:
            if current._data == element:
                self.remove(element)
                
            current = current._next
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        #your code goes here


    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the List. The list contains
        one and only one of each value formerly present in the list.
        The first occurrence of each value is preserved.
        Use: sl.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        current = self._head
        previous = None
        visited = []
        
        while current is not None:
            if current._data not in visited:
                
                visited.append(current._data)
                previous = current
                
            else:
                
                previous._next = current._next
                self._count -= 1
                
            current = current._next
            
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = lst.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        current = self._head
        target_current = target._head
        counter = 0
        identical = False
        
        while current != None and target_current != None:
            if current._data ==  target_current._data:
                counter += 1
                
            target_current = target_current._next
            current = current._next
            
        if counter == self._count:
            identical = True
            
        return identical        

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        The values are added to the current List.
        (iterative algorithm)
        Use: lst.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        current = source1._head
        
        while current is not None:
            
            previous = source2._head
            
            while previous is not None:
                
                if current._data == previous._data and self.__contains__(current._data) == False:
                    
                    self.append(current._data)
                    
                previous = previous._next
                
            current = current._next
        

    
    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        The values are added to the current List.
        (iterative algorithm)
        Use: lst.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        current = source1._head
        previous = source2._head 
        
        while current is not None:
            
            self.append(current._data)
            
            current = current._next
            
        while previous is not None:
            
            if self.__contains__(previous._data) == False:
                
                self.append(previous._data)
                
            previous = previous._next
            
        self.clean()
                

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into the current List and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: lst.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        #your code goes here

    def split(self):
        """
        -------------------------------------------------------
        Splits the current List into two parts. target1 contains the
        first half, target2 the second half. The self List (current
        List) becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        #your code goes here




    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the current list into separate target lists with data
        elements alternating into the targets. At finish the current 
        List is empty.
        Order of the data elements is preserved.
        (iterative algorithm)
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from self List (List)
            target2 - contains other alternating values from self List (List)
        -------------------------------------------------------
        """
        #your code goes here


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from head to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._head

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
        current = self._head
 
        while current is not None:
            print(current._data)
            current = current._next
        return

        
