# Imports
from copy import deepcopy
from BST import BST

# Constants
SEP = '-' * 40

class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, size):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of containing size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Parameter:
            size - number of initial slots in the hash table (int > 0)
        Returns:
            A new HashSet object (HashSet)
        -------------------------------------------------------
        """
        self._TableSize = size
        self._table = [None] * self._TableSize
        self._count = 0

        for i in range(self._TableSize):
            self._table[i] = BST()


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of elements in the HashSet.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of elements in the HashSet.
        -------------------------------------------------------
        """
        return self._count

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if the HashSet is empty.
        Use: b = hs.isEmpty()
        -------------------------------------------------------
        Returns:
            True if the HashSet is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _hashfunction(self, element):
        """
        -------------------------------------------------------
        Returns the index in the table where the element can
        be inserted.        
        Use: list = self._hashfunction(element)
        -------------------------------------------------------
        Returns:
            index - the position of the element in self._table
        -------------------------------------------------------
        """
        key = hash(element) #returns an integer key for the element 
        return key % self._TableSize        

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        slot_list = self._hashfunciton(key)
        return key in slot_list

    def insert(self, element):
        """
        ---------------------------------------------------------
        Inserts the given element into the Hash Set, allows only
        one copy of element        .
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(element)
        -------------------------------------------------------
        Parameters:
            element - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        
        index = self._hashfunction(element)
        slot_list = self._table[index] 

        # Doesnt insert data if its already in the hash set`     
        if element in slot_list:
       
            inserted = False
        else:
            inserted = True
            self._count += 1
            slot_list.insert(element)


            # Checks the load factor, will rehash is necassry 
            if self._count > (HashSet._LOAD_FACTOR * self._TableSize):
                self._rehash()
        
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the element identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        value = None
        index = self._hashfunction(key)
        slot_table = self._table[index]

        if key in slot_table:
            value = deepcopy(key)
        
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        value = False
        index = self._hashfunction(key)
        slot_table = self._table[index]

        if key in slot_table:
            slot_table.delete(key)
            self._count -= 1
            value = True

        
        return value
    
    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and
        reallocates the  existing data within the Hash Set to the
        new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        CHANGE_FACTOR = 2 * self._TableSize + 1    
        slots = CHANGE_FACTOR - self._TableSize    
        self._TableSize = CHANGE_FACTOR    
            
        for i in range(slots):    
            self._table.append(BST())    
            
        for i in self._table:    
            for j in i:    
                if j is not None:    

                    h = hash(j)    
                    index = h % self._TableSize    
                    slot_table = self._table[index]   
                     
                    if j not in slot_table:    
                        slot_table.insert(j)    
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
