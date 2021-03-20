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
# pylint: disable=W0212

# Imports
from copy import deepcopy


class SortedList:
    DEFAULT_SIZE = 5
    def __init__(self, max_size=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: slst = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
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
        Determines if List is empty.
        Use: b = slst.is_empty()
        -------------------------------------------------------
        Returns:
            True if slst is empty, False otherwise.
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
 

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted List.
        Use: n = len(slst)
        -------------------------------------------------------
        Returns:
            the number of data elements in sorted List.
        -------------------------------------------------------
        """
        
        return self._count


    def insert(self, element):
        """
        -------------------------------------------------------
        A copy of element is inserted at the proper place in List.
        Consecutive insertions of the same value must keep their 
        order preserved.
        Use: slst.insert(data element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            True if insert is successful, False otherwise.
        -------------------------------------------------------
        """
        assert not self.isFull(), "List is full"

        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = self._count - 1

        while low <= high:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if self._values[mid] > element:
                # search the left subarray.
                high = mid - 1
            else:
                # Default: search the right subarray.
                low = mid + 1
        
        i = low
        #insert at position i

        j =0
        if i == self._count:                      #insertion at end of array
            self._values[i] = deepcopy(element)
        else:                                      #general insertion
            for j in range(self._count, i-1, -1):  #shift element to make space for new element
                self._values[j] = self._values[j-1]
            self._values[i] = deepcopy(element)           
        self._count += 1                            #increment number of elements
        return 
       
    def _binary_search(self, element):
        """
        -------------------------------------------------------
        Searches for the first occurrence of element in the sorted list.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            element - a data element to search for (?)
        Returns:
            i - the index of the first occurrence of the element in
                the list, -1 if the element is not found. (int)
        -------------------------------------------------------
        """
        # Index of beginning of subarray to search.
        low = 0
        # Index of end of subarray to search.
        high = self._count - 1

        while low < high:
            # Find the middle of the current subarray.
            # (avoids overflow on large values vs (low + high)//2
            mid = (high - low) // 2 + low

            if element > self._values[mid] :
                # Search the right subarray.
                low = mid + 1
            else:
                # Default: search the left subarray.
                high = mid

        # Deferred test for equality.
        if low == high and self._values[low] == element:
            i = low
        else:
            i = -1
        return i

    def remove(self, element):
        """
        -------------------------------------------------------
        Findd and removes the first element in the List that
        matches the given element.
        Use: b = slst.remove(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            b - True if remove succesful, False otherwise
        -------------------------------------------------------
        """
        
        
        assert not self.isEmpty(), "cannot remove from an empty List"
        
        
        state = False
        count = 0;
        
        for i in self._values:
            if element == i:
                state = True
                for i in range(count,self._count-1,1):
                    self._values[i] = self._values[i+1]
                    self._values[i+1] = None  
            count += 1
        self._count = self._count - 1
        return state         

    def find(self, element):
        """
        -------------------------------------------------------
        Finds and returns a copy of element in the List  that 
        matches the given element.
        Use: b = slst.find(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            b - True if find the element, False otherwise
        -------------------------------------------------------
        """
        
        i = self._binary_search(element)

        return i > -1

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first data element in the List .
        Use: value = slst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first data element in the List (?)
        -------------------------------------------------------
        """
        
        assert not self.isEmpty(), "Cannot peek at an empty List"

        element = deepcopy(self._values[0])
        return element

    def indexOf(self, element):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of the element
        in the List.
        Use: n = slst.index(element)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            i - the location of the data element matching the 
            given element, otherwise -1 (int)
        -------------------------------------------------------
        """

        index = self._binary_search(element)
        
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
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        
        state = False
        
        if i < self._count and i >= self._count * -1:
            state = True
            
        return state 
    

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the List.
        Use: value = slst[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of slst (?)
        -------------------------------------------------------
        """
        
        assert self._is_valid_index(i), "Invalid index: out of range"

        if i < 0:
            i = self._count + i
        value = deepcopy(self._values[i])
        return value

    def __contains__(self, element):
        """
        ---------------------------------------------------------
        Determines if the List contains the given data element.
        Use: b = element in slst
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if slst contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        
        i = self._binary_search(element)
        return i > -1



    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum data element in the List.
        Use: value = slst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum data element in the List (?)
        -------------------------------------------------------
        """
                                
        value = deepcopy(self._values[self._count -1 ])
                
        return value



    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum data value in the List.
        Use: value = slst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum data element in source (?)
        -------------------------------------------------------
        """
                
        
        value = deepcopy(self._values[0])
        
        return value


   
    def count(self, element):
        """
        -------------------------------------------------------
        Determines the number of times the given element appears 
        in the List.
        Use: n = slst.count(key)
        -------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            number - the number of times element appears in slst (int)
        -------------------------------------------------------
        """
        number = 0
        
        for i in range(self._capacity):
            if element == self._values[i]:
                number += 1
                
        return number



    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the List. The List will contain one and only one
        of each value formerly present in the List source. The first occurrence
        of each value is preserved.
        Use: slst.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        count = 0
        
        new_list = SortedList(self._capacity)
        
        for i in self._values:
            if i not in new_list._values:
                new_list.insert(i)
            count += 1
                
        self._values = new_list._values
        self._count = new_list._count
        


    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with copies of data elements 
        that appear in both source1 and source2. Values do not
        repeat.
        Use: slst.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        new_lst = SortedList(self._capacity)
        
        for i in range(source1._count):
            for j in range(source2._count):
                
                if source1._values[i] == source2._values[j]:
                    if source1._values[i] not in new_lst._values:
                        new_lst.insert(source1._values[i])
                    
        self._values = new_lst._values
        self._count = new_lst._count
        

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        both source1 and source2. Values do not repeat.
        Use: slst.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        new_lst = SortedList(self._capacity)
        
        for i in source1._values:
             
            if i not in new_lst._values:
                 
                new_lst.insert(i)
         
        for i in source2._values:
             
            if i not in new_lst._values:
                 
                    new_lst.insert(i)
        

                
        self._values = new_lst._values
            
        self._count = new_lst._count



    def remove_many(self, element):
        """
        ---------------------------------------------------------
        Removes all values in the List that match the given element
        Use: slst.remove_many(element)
        ---------------------------------------------------------
        Parameters:
            element - the element key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        
        
        counter = 0
        
        for i in self._values:
            
            
            if i == element:
                
                
                counter += 1;
        
        for i in range(counter):
            
            self.remove(element)



    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        Order of target1 and target2 is not significant.
        The List is empty after the function executes.
        (iterative version)
        Use: target1, target2 = slst.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = SortedList()
        target2 = SortedList()
        
        for i in range(self._count):
            if i % 2 == 0:
                target1.insert(self._values[i])
            else:
                target2.insert(self._values[i])
                
        for i in range(self._capacity):
            self._values[i] = None
            
            
            
        self._count = 0
        
        
        return target1, target2


    def split(self):
        """
        ---------------------------------------------------------
        Splits the List into two parts. target1 contains the first half,
        target2 the second half. The List becomes empty.
        Use:  target1, target2 = slst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        target1 = SortedList()
        target2 = SortedList()
        
        midpoint = (self._count // 2) +1 
        
        if midpoint < 1 and self.isEmpty() == False:
            midpoint = 1
        
        for i in range(midpoint):
            target1.insert(self._values[i])
            
        for i in range(midpoint, self._count):
            target2.insert(self._values[i])
            
        for i in range(self._capacity):
            self._values[i] = None
            
        target1._count = midpoint
        target2._count = midpoint
        
        self._count = 0
        
        
        return target1, target2



    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits a List into two parts. target1 contains all values < key,
        target2 all values >= key. The List becomes empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        # your code goes here



    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits a List into two parts. target1 contains all the values
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, the List is empty. Order of values
        in targets is maintained.
        Use: target1, target2 = slst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # your code goes here



    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of the List to another sorted list.
        Use: target = slst.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents
                of the List (Sorted_List)
        -------------------------------------------------------
        """
        # your code goes here



    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current list.
        When finished, the contents of source1 and source2 are interlaced
        into the current List and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: slst.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code goes here



    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = slst.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List)
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

            



    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first data element in the List.
        Use: value = slst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first data element in the list (?)
        -------------------------------------------------------
        """
        # your code goes here
        value = self._values[self._front]
        
        self.remove(value)
        
        return value        




    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

        # your code goes here


