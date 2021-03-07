"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Zeel Patel
ID:     200881210
Email:  pate1210@mylaurier.ca
__updated__ = '2021-01-31'
------------------------------------------------------------------------
"""
# Imports
from copy import deepcopy
from pickle import NONE


class List:

    DEFAULT_SIZE = 10

    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty List.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        assert max_size > 0, "List size must be > 0"

        self._capacity = max_size
        self._values = [None] * self._capacity
        self._count = 0
        self._front = 0
        self._rear = 0
        

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the List is empty.
        Use: empty = lst.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the List is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0
    
    def isFull(self):
        """
        -------------------------------------------------------
        Determines if the List is full.
        Use: b = lst.isFull()
        -------------------------------------------------------
        Returns:
            True if the List is full, False otherwise.
        -------------------------------------------------------
        """

        
        return self._count >= self._capacity
 
    def size_(self):
        """
        -------------------------------------------------------
        Returns the number of data elements in the List.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of data elements in the List.
        -------------------------------------------------------
        """
        return self._count

   
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of data elements in the List.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of data elements in the List.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, i, element):
        """
        -------------------------------------------------------
        A copy of element is inserted at index i, following 
        data items are shifted to the right. If i is outside 
        of range   of -len(List) to len(List) - 1, the method halts
        by calling assertion.
        Note: Python allows negative indices for Python list and 
        we want to support it for our List implementation

        Use: lst.insert(i, element)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            element - a data element (?)
        Returns:
            True if insert is successful, False otherwise.
        -------------------------------------------------------
        """
#         assert self._is_valid_index(i), "invalid indices"
# 
#         assert self._count< self._capacity, "List is full"
        
        if i < 0:
            i = self._count + i

        #TODO: make it work for negative index
        #TODO: if array is full 
        
        
        if self._count == self._capacity:
            new_lst = List()
            new_lst._capacity = self._capacity*2
            new_lst._values = [None] * (self._capacity*2)
            
#             new_lst = deepcopy(self)
            
            for i in range(self._count):
                new_lst._values[i] = deepcopy(self._values[i])
                
            self._capacity = new_lst._capacity
            self._values = new_lst._values
        
#         if self.isFull():
#             new_list = List(self._capacity * 2)
#              
#             for i in range(self.size_()):
#                 new_list.append(self._values[i])
#                 
#             new_list = self

        #insert if there is room in place
        j =0
        if i == self._count:                      #insertion at end of array
            self._values[i] = deepcopy(element)
        else:                                      #general insertion
            for j in range(self._count, i-1, -1):  #shift element to make space for new element
                self._values[j] = self._values[j-1]
            self._values[i] = deepcopy(element)           
        self._count += 1                            #increment number of elements
        
        
        return self._is_valid_index(i)


    def prepend(self, element):
        """
        -------------------------------------------------------
        Adds a copy of data element to the front of the List.
        Use: lst.prepend(element)
        -------------------------------------------------------
        Parameters:
            element - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        

        for i in range(self._count -1, -1, -1):
            
            
            self._values[i + 1] = self._values[i]
            
        self._count +=1 
            

        self._values[self._front] = deepcopy(element)
        
        
            
        
        #your code goes here
        

    def append(self, element):
        """
        ---------------------------------------------------------
        Adds a copy of data element to the end of the List.
        Use: lst.append(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
    
        
        self._values[self._count] = deepcopy(element)
        
        self._count += 1
        


    def _linear_search(self, element):
        """
        -------------------------------------------------------
        Searches for the first occurrence of element in the List.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            i - the index of element in the List, -1 if element
             is not found (int)
        -------------------------------------------------------
        """
        
        value = -1
        
        i = 0
        while i < self._count:
            if self._values[i] == element:
                value = i   
            i += 1     
        

        return value
            
 
    def remove(self, element):
        """
        -------------------------------------------------------
        Finds and removes the first data element in List that
        matches the given element.
        Use: b = lst.remove(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            True if remove is successful, False otherwise
        -------------------------------------------------------
        """
        assert not self.isEmpty(), "cannot remove from an empty List"

        index = self._linear_search(element)

        if index > -1:
            i = 0
            for i in range(index, self._count - 1):
                self._values[i] = self._values[i+1]
            self._values[ self._count - 1] = None
            self._count -= 1
            ret = True 
        else:
            ret = False
        return ret

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
        i = self._linear_search(element)

        return i > -1
    

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first data element in the List; i.e.,
        the data element at the front of the List
        Use: element = lst.peek()
        -------------------------------------------------------
        Returns:
            element - a copy of the first value in the List (?)
        -------------------------------------------------------
        """
        assert not self.isEmpty(), "Cannot peek at an empty List"

        element = deepcopy(self._values[0])
        return element

    def indexOf(self, element):
        """
        -------------------------------------------------------
        Finds location of the given data element in the List.
        Use: n = lst.indexOf(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            i - the index of the location of element in the 
            List, -1 if element is not in the List. (int)
        -------------------------------------------------------
        """
        
        index = self._linear_search(element)
        
        counter = 0;
        value = -1;
        
        
        for i in range(self._count):
            if element == self._values[i]:
                value = counter
            counter += 1
        
        return value


    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(List) to len(List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        
        state = False
#        
        if i <= self._count and i >= self._count*-1:
                state = True
        
        if self.isEmpty() or i > self._count - 1:
            state = False

        return state


    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the i-th element of the List.
        Use: value = lst[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of List (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index: out of range"

        if i < 0:
            i = self._count + i
        value = deepcopy(self._values[i])
        
        return value

    def __setitem__(self, i, element):
        """
        ---------------------------------------------------------
        Sets the i-th element of the List to contain a copy of 
        the given element. The existing value at position i is 
        overwritten.
        Use: lst[i] = element
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        if i < 0:
           
            i = self._count + i
            
        self._values[i] = deepcopy(element)
        


    def __contains__(self, element):
        """
        ---------------------------------------------------------
        Determines if the List contains the given data element.
        Use: b = element in lst
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            True if the List contains element, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._linear_search(element)
        state = False
        
        if i != -1:
            state = True
            
        
        return state

    def max(self):
        """
        -------------------------------------------------------
        Finds the data element with maximum value in List.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the List (?)
        -------------------------------------------------------
        """
        
        assert not self.isEmpty()

        value = -999999999999
        
        temp = self._values[0]
        
        for i in range(self.size_()):
            if self._values[i] > temp :
                temp  = self._values[i]
                
        value = deepcopy(temp)
                
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the data element with minimum value in List.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the List (?)
        -------------------------------------------------------
        """
#         value = 999999999999
#         
#         for i in range(self.size_()):
#             if self._values[i] < value:
#                 value = self._values[i]
#                 
#         return value

        assert not self.isEmpty()

        temp = self._values[0];
        for i in range(self._count):
            if self._values[i] < temp:
                temp = self._values[i]
        
        
        value = deepcopy(temp)
        
        return value


    def count(self, element):
        """
        -------------------------------------------------------
        Finds the number of times the given data element appears
        in the List.
        Use: n = lst.count(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            number - number of times element appears in List (int)
        -------------------------------------------------------
        """
        
        number = 0
        
        for i in range(self.size_()):
            if element == self._values[i]:
                number += 1
                
        return number
        


    def reverse(self):
        """
        -------------------------------------------------------
        The contents of the List are reversed in order with respect
        to their order before the operation was called.
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
        Modifies the List so that it contains one and only one copy
        of each value formerly present in the List. The first
        occurrence of each value is preserved.
        Use: lst.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        count = 0
        
        new_list = List(self._capacity)
        
        for i in self._values:
            if i not in new_list._values:
                new_list.insert(count,i)
            count += 1
                
        self._values = new_list._values
        self._count = new_list._count
            
        
        



    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns the first data element from the List.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first data element in the List (?)
        -------------------------------------------------------
        """
        
        value = self._values[self._front]
        
        self.remove(value)
        
        return value
        
        #you code goes here
    
    def remove_many(self, element):
        """
        -------------------------------------------------------
        Finds and removes all data element in the List that match 
        the given element.
        Use: lst.remove_many(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        counter = 0
        for i in self._values:
            
            
            if i == element:
                
                
                counter += 1;
        
        for i in range(counter):
            
            self.remove(element)
        
        
#         counter = 0
# 
#         for i in range(self._values):
#              
#             if self._values[i] == element:
# 
#                 counter += 1
#                 
#             
#         for i in range(counter):
#             
#             self.remove(element)

               
            

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether this List (e.g., lst) is identical to the  
        the target List, i.e. same values appear in the same locations 
        in both  Lists. (iterative version)
        Use: b = lst.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another List (List)
        Returns:
            identical - True if this List contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        
        count = 0
        identical = False
        
        
        for i in range(self._count):
            if self._values[i] == target._values[i]:
                count += 1
                
        if count == self._count and self.isEmpty() == False:
            identical = True
            
        if target.isEmpty() and self.isEmpty():
            identical = True
            
        return identical
            
            
        
    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update this List (lst) with all data elements that appear 
        in both source1 and source2, The data elements  do not 
        repeat.
        Use: lst.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based List (List)
            source2 - an array-based List (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        new_lst = List(self._capacity)
        
        for i in range(source1._count):
            for j in range(source2._count):
                
                if source1._values[i] == source2._values[j]:
                    new_lst.insert(new_lst._count, source1._values[i])
                    
        self._values = new_lst._values
        self._count = new_lst._count
        
    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update this List (lst) with all data elements that appear in
        source1 or source2. Values do not repeat.
        Use: lst.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based List (List)
            source2 - an array-based List (List)
        Returns:
            None
        -------------------------------------------------------
        """
        new_lst = List(self._capacity)
#         
        for i in source1._values:
             
            if i not in new_lst._values:
                 
                new_lst.insert(new_lst._count, i)
         
        for i in source2._values:
             
            if i not in new_lst._values:
                 
                    new_lst.insert(new_lst._count, i)
        

                
        self._values = new_lst._values
            
        self._count = new_lst._count
        
        
        
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits this List (e.g., lst) into two separate target Lists 
        with values alternating into the targets. At finish this 
        List (lst) is empty. Order of values in lst is preserved.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from lst (List)
            target2 - contains other alternating values from lst (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        for i in range(self._count):
            if i % 2 == 0:
                target1.append(self._values[i])
            
        for i in range(self._count):
            if i % 2 != 0:
                target2.append(self._values[i])
                
        for i in range(self._capacity):
            self._values[i] = None
        
        self._count = 0
        return target1, target2

    def split(self):
        """
        -------------------------------------------------------
        Splits this List (lst) into two parts. target1 contains the
        first half, target2 the second half. Source List becomes empty.
        Order of values is preserved.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        
        target1 = List()
        target2 = List()
        
        if self._count % 2 == 1:
            midpoint = (self._count // 2) + 1
            
        else:
            midpoint = self._count // 2
            
        
        for i in range(midpoint):
            target1.append(self._values[i])
            
        for i in range(midpoint, self._count):
            target2.append(self._values[i])
            
        for i in range(self._capacity):
            self._values[i] = None
            
        self._count = 0
            
        target1._count = midpoint
        target2._count = midpoint
        
        return target1, target2
                
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source Lists into this List (lst).
        When finished, the contents of source1 and source2 are 
        interlaced into this List and source1 and source2 are empty.
        Order of source1 and source2 values is preserved.
        Use: lst.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based List (List)
            source2 - an array-based List (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        temp = 0
        
        if source1._count > source2._count:
            temp = source1._count
        else:
            temp = source2._count
        for i in range(temp + 1):
            if source1._values[i] != None:
                self.append(source1._values[i])
            if source2._values[i] != None:
                self.append(source2._values[i])
                
        for i in range(source1._capacity):
            source1._values[i] = None
            
        source1._count = 0
            
        for i in range(source2._capacity):
            source2._values[i] = None
            
        source2._count = 0
        return 

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the List
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the List (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
            
            
            

        

