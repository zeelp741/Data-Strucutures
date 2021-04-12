# Imports
from copy import deepcopy

class BSTNode:

    def __init__(self, data):
        """
        -------------------------------------------------------
        Initializes a BST node containing the data. Child pointers
        are None
        Use: node = BSTNode(element)
        -------------------------------------------------------
        Parameters:
            data - data for the node (?)
        Returns:
            A BSTNode object (BSTNode)
        -------------------------------------------------------
        """
        self._data = deepcopy(data)
        self._left = None
        self._right = None        

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node data as a string - for debugging.
        -------------------------------------------------------
        """
        
        #return "h: {}, v: {}".format(1, self._data)
        return "{} {} {}".format("{",self._data, "}")


class BST:
    
    def display(self):
        self.display_aux("", self._root, 0)
    
    def display_aux(self, prefix, T, isLeft):              
        if (T is not None):
            print(prefix, end='')
            if isLeft==1:
                print("├──", end='')
            else:  
                print("└──", end='')

            print(T._data, "\n ")
          

            temp=""
            if isLeft==1 :
                temp = prefix+  "|    "
            else:
                temp = prefix +  "    "

            self.display_aux(temp, T._right, 1)
            self.display_aux(temp, T._left, 0) 
             

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None        

    def isEmpty(self):
        """
        -------------------------------------------------------
        Determines if BST is empty.
        Use: b = bst.isEmpty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def size(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = bst.size(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in bst.
        -------------------------------------------------------
        """
        return self._count

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in bst.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, element):
        """
        -------------------------------------------------------
        Inserts a copy of data element into BST. The data element
        may appear only once in the tree. The main job is done
        inside the recursive method _insert_aux. The BST tree is 
        updated
        Use: bst.insert(element)
        -------------------------------------------------------
        Parameters:
            element - data to be inserted into bst (?)
        Returns:
            None 
        -------------------------------------------------------
        """
        self._root = self._insert_aux(self._root, element)
        return None        

    def _insert_aux(self, bstnode, element):
        """
        -------------------------------------------------------
        Inserts a copy of the data element into the binary 
        search tree rooted at bstnode. Private recursive 
        operation called only by insert method.
        Use: node = self._insert_aux(bstnode, element)
        -------------------------------------------------------
        Parameters:
            bstnode - a BSTNode (BSTNode)
            element - data element to be inserted into the 
            subtree rooted at node (?)
        Returns:
            node - the updated bstnode (BSTNode)            
        -------------------------------------------------------
        """
        if bstnode is None:
            # Base case: add a new node containing the value.
            bstnode = BSTNode(element)
        elif element < bstnode._data:
            # General case: check the left subtree.
            bstnode._left = self._insert_aux(bstnode._left, element)
        elif element > bstnode._data:
            # General case: check the right subtree.
            bstnode._right = self._insert_aux(bstnode._right, element)
        else:            
            print("The element is already in the tree")                                                
        return bstnode 
    
    def find(self, element):
        """
        -------------------------------------------------------
        Returns the node in the BST containing the given element.
        Returns None if the BST does not contain this element.
        (Iterative)
        Use: node = bst.find(element)
        -------------------------------------------------------
        Parameters:
            element - element to search for (?)
        Returns:
            node - The node containing the given element, None if
            the element is not found             
        -------------------------------------------------------
        """
        node = self._root
        
        while node is not None:

            if node._data > element:
                node = node._left
            elif node._data < element:
                node = node._right
            else:
                if node._data==element:
                    return node 
                           
        return None

    def findMin(self, bstnode):
        """
        -------------------------------------------------------
        Return the node containing the minimum data element
        in the subtree rooted at bstnode. Starting at the 
        bstnode, it keeps moving to the left until it reaches 
        a node that has no left child and returns that ndoe.
        (Iterative)        
        Use: b = bst.findMin(element)
        -------------------------------------------------------
        Parameters:
            bstnode - the root of the bst (?)
        Returns:
            node - the node containing the minimum data element
            in the tree rooted at bstnode            
        -------------------------------------------------------
        """        
        node = bstnode    
        if node is not None:        
            while node._left is not None:
                node = node._left        
                    
        return node  
    
    def delete(self, element):
        """
        -------------------------------------------------------
        deletes the node containing the given element from BST.
        The job of deleting is done in _delete_aux method. 
        Updates structure of BST as required.
        Use: bst.delete(element)
        -------------------------------------------------------
        Parameters:
            element - data element to be deleted (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._root = self._delete_aux(self._root, element)
        return 

    def _delete_aux(self, bstnode, element):         
        """
        -------------------------------------------------------
        deletes the node containing the data element in the
        subtree rooted at bstnode. Updates structure of BST as 
        required. Private recursive method called by delete.
        Use: bstnode = self._delete_aux(bstnode, element)
        -------------------------------------------------------
        Parameters:
            bstnode - a node in the BST (BSTNode)
            element - data element in the node to be removed (?)
        Returns:
            bstnode - the updated bstnode
        -------------------------------------------------------
        """
        if bstnode is None: #BST is empty
            return bstnode
        elif element < bstnode._data:
            bstnode._left = self._delete_aux(bstnode._left, element)
        elif element > bstnode._data:
            bstnode._right = self._delete_aux(bstnode._right, element)
        else:   #node to be deleted is found                        
            if bstnode._left and bstnode._right: #node has two children                
                #replace with smallest in right subtree
                tempNode = self.findMin( bstnode._right )
                bstnode._data = tempNode._data
                bstnode._right = self._delete_aux(bstnode._right, bstnode._data)
                print("tempNode._data=", tempNode._data)
            else: #node has zero or one child
                tempNode = bstnode
                if bstnode._left is None:
                    bstnode = bstnode._right
                elif bstnode._right is None:
                    bstnode = bstnode._left                                                            
        return bstnode

    def inorder(self):
        """
        -------------------------------------------------------
        Returns a Python list containing the contents of the tree
        in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (Python list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses subtree rooted at node in inorder. 
        a contains the contents subtree rooted at node and in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
            a - list containing the content of subtree rooted at node (list of ?)
        Returns:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(node._data)
            self._inorder_aux(node._right, a)

        return

    def preorder(self):
        """
        -------------------------------------------------------
        Returns a Python list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (Python list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses the subtree rooted at node in preorder. 
        a contains the contents of subtree rooted at node in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
            a - list containing the content of the subtree rooted at node (list of ?)
        Returns:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(node._data)
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)

        return

    def postorder(self):
        """
        -------------------------------------------------------
        Returns a Python list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._postorder_aux(self._root, a)
        return a

    def _postorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses subtree rooted at node in postorder. 
        a contains the contents of subtree rooted at node in postorder.
        Private recursive operation called only by postorder.
        Use: self._postorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - list containing the content of the subtree rooted at node (list of ?)
        Returns:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left, a)
            self._postorder_aux(node._right, a)
            a.append(node._data)

        return   

    def levelorder(self):
        """
        -------------------------------------------------------
        Returns a Python list containing the contents of the tree
        in levelorder order.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the contents of bst in levelorder.
            (Python list of ?)
        -------------------------------------------------------
        """
        values = []

        if self._root is not None:
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                node = queue.pop(0)
                values.append(node._data)

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)

        return values


    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether the bst is balanced, i.e. for each node in
        the bst the difference between its left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            is_balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        is_balanced = self._is_balanced_aux(self._root)
        return is_balanced

    def _is_balanced_aux(self, node):
        """
        ---------------------------------------------------------
        Determines whether the subtree rooted at node is balanced.
        Private operation called only by is_balanced.
        Use: b = self._is_balanced_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - the root of the subtree to check its balance (BSTNode)
        Returns:
            is_balanced - True if node is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        #Base case: 
            # No node exists
        if node is None:
            is_balanced = True
        else:
                # Checks if left tree is balanced
            left = self._is_balanced_aux(node._left)
                # Checks if right tree is balanced
            right = self._is_balanced_aux(node._right)

            is_balanced = abs(left - right) <= 1

        return is_balanced


    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another bst (BST)
        Returns:
            identical - True if this bst contains the same elements
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        return self._is_identical_aux(self._root, other._root)

    def _is_identical_aux(self, node1, node2):
        """
        ---------------------------------------------------------
        Determines whether two subtrees rooted at node1 and node2
        are identical.
        Use: b = self._is_identical_aux(node1, node2)
        -------------------------------------------------------
        Parameters:
            node1 - root of the current BST (BSTNode)
            node2 - root of the other BST (BSTNode)
        Returns:
            identical - True if the subtree rooted at node1 contains 
                the same elements as the other subtree rooted at node2
                in the same order, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        if node1 is None or node2 is None:
            if node1 is None and node2 is None:
                identical = True
            else:
                identical = False

        elif node1._left is None:
            if node2._left is None:
                identical = True
            else:
                identical = False

        elif node1._right is None:
            if node2._right is None:
                identical = True
            else:
                identical = False

        else:
            identical = self._is_identical_aux(node1._left, node2._left) and self._is_identical_aux(node1._right, node2._right)
        return identical

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. for each node
        the element in its left node is smaller than theelement 
        in the node and the element in the right node is larger 
        than the element in the node.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        return self._is_valid_aux(self._root)

    def _is_valid_aux(self, node):
        """
        ---------------------------------------------------------
        Determines if the subtree rooted at node is a valid BST.
        Use: b = self._is_valid_aux(self._root)
        ---------------------------------------------------------
        Parameters:
            node - a binary tree node (BSTNode)
        Returns:
            valid - True if node is root of a valid BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
            # Base case:
                # Node doesnt exist    
        if node is None:
            valid = True
        elif node._left is None:
                # Node doens't have a left subtree
            valid = True
        elif node._right is None:
                # Node doesn't have a right subtree
            valid = True
        else:
                # Node has two children
            valid = False


                # Checks to see if left child is smaller than right
            if node._left._data < node._data:
                valid = True

                # Check to see if right node is greater than current node
            if node._right._data > node._data and valid:
                valid = True

                # Height should be 
            height = self._node_height(node)
            if height == node._height + 1:
                valid = True
            
        return valid
    
    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum element in BST. (Iterative algorithm)
        Use: element = bst.min()
        -------------------------------------------------------
        Returns:
            element - a copy of the minimum element in the BST (?)
        -------------------------------------------------------
        """
        node = self._root
        parent = None

        while node is not None:
            parent = node
            node = node._left

        element = parent._data
        return element
    
    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        return self._leaf_count_aux(self._root)

    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in 
        subtree rooted at node. Private helper method.
        Use: count = self._leaf_count_aux(self._root)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            count - number of nodes with no children is subtree 
                rooted at node (int)
        ---------------------------------------------------------
        """
        if node is None:
            count = 0
        
        elif node._left is None and node._right is None:
            count = 1

        else:
            count = self._leaf_count_aux(node._left) + self._leaf_count_aux(node._right)
        
        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes with one child in the BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        return self._one_child_count_aux(self._root)

    def _one_child_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes with one child in subree rooted
        at node.
        -------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            count - number of nodes with one child in subtree rooted 
                at node (int)
        ----------------------------------------------------------
        """

        if node is None:
            count = 0

        elif not node._right is None and node._left is None:
            count = 1 + self._one_child_count_aux(node._right)

        elif not node._left is None and node._right is None :
            count = 1 + self._one_child_count_aux(node._left)

        else:
            count = self._one_child_count_aux(node._left) + self._one_child_count_aux(node._right)
        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes with two children in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        return self._two_child_count_aux(self._root)

    def _two_child_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes with two children in the subtree
        rooted at node. Private helper method.
        -------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            count - number of nodes with two children in subtree 
                rooted at node (int)
        ----------------------------------------------------------
        """

        if node is None:
            count = 0

        elif node._right is not None and node._left is not None:
            count = 1 + self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)

        else:
            count = self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)

        return count
    
    def remove_root(self):
        """
        -------------------------------------------------------
        Removes the root node and returns the data element in it.
        Use: element = bst._remove_root()
        -------------------------------------------------------
        Returns:
            element - the data element in root.
        -------------------------------------------------------
        """
        #your code goes here
    
    def __contains__(self, element):
        """
        ---------------------------------------------------------
        Determines if bst contains the given element.
        Use: b = element in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise (boolean)
        -------------------------------------------------------
        """
        value = self.find(element)
        return value is not None

    def height(self):
        """
        -------------------------------------------------------
        Returns the height of a BST, i.e. the length of the
        longest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            h - height of bst (int)
        -------------------------------------------------------
        """
        #your code goes here

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the element in the parent node of the node containing
        the given key in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            element - a copy of the element in a node that is the parent of the
            node containing key, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # Find the node containing the key.
        node = self._root
        parent = None
        found = False

        while node is not None and found is False:

            if key < node._data:
                parent = node
                node = node._left

            elif key > node._data:
                parent = node
                node = node._right

            else:
                found = True

        if parent is None or not found:
            element = None

        else:

            element = deepcopy(parent._data)
        return element

    def parent_r(self, element):
        """
        ---------------------------------------------------------
        Returns the _data in the parent node of the node containing 
        the given element in a bst.
        ---------------------------------------------------------
        Parameters:
            element - a data element (?)
        Returns:
            data - a copy of the _data in a node that is the parent of the
            node containing element, None if the node does not have a 
            parent.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        # Find the node containing the key _value.
        return self._parent_aux(self._root, element, None)


    def _parent_aux(self, node, element, parent):
        """
        ---------------------------------------------------------
        Returns the _data in the parent of the node containing the
        given element in a bst rooted at node.
        Private recursive operation called only by parent_r.
        Use: e = self._parent_aux(node, key, parent of node)
        ---------------------------------------------------------
        Parameters:
            node - a BST node
            element - a  data element
            parent - the parent of the node
        Returns:
            data - the _data of the parent node, None if it has no parent (?)
        ---------------------------------------------------------
        """
        if node is None:

            value = None
        elif element < node._data:

            value = self._parfent_aux(node._left, element, node)
        elif element > node._data:

            value = self._parent_aux(node._right, element, node)
        elif parent is None:

            value = None
        else:

            value = deepcopy(parent._data)
        return valuefn

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum data element n BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            element - a copy of the maximum element in the BST (?)
        -------------------------------------------------------
        """
        #your code goes here

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest element in a bst. (Recursive algorithm)
        Use: element = bst.max_r()
        ---------------------------------------------------------
        Returns:
            element - a copy of the maximum element in the BST (?)
        ---------------------------------------------------------
        """
        #your code goes here

    def _max_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the largest element in a BST rooted at node. 
        (Recursive algorithm). Private helper method.
        Use: v = self._max_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - the root of the subtree to look for its max (BSTNode)
        Returns:
            element - a copy of the largest data element in 
                the subtree rooted at node (?)
        ---------------------------------------------------------
        """
        #your code goes here


    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            element - a copy of the minimum element in the BST (?)
        ---------------------------------------------------------
        """

        #your code goes here

    def _min_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the minimum data element in a subtree rooted at
        node. (Recursive algorithm)
        Use: v = self._min_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            element - a copy of the minimum data element in the
                 subtree rooted at node (?)
        ---------------------------------------------------------
        """

        #your code goes here

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST:
        leaf nodes, node with one child, and nodes with two children.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one -  number of nodes with one child (int)
            two -  number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero, one, two = self._node_counts_aux(self._root)
        return zero, one, two

    def _node_counts_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a 
        subtree rooted at node.
        -------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            zero - number of nodes with zero children (int)
            one -  number of nodes with one child (int)
            two -  number of nodes with two children (int)
        ----------------------------------------------------------
        """
        if node is None:

            one = 0
            two = 0
            zero = 0

        elif node._left is None and node._right is None:

            one = 0
            two = 0
            zero = 1

        elif node._left is not None and node._right is None:

            zero, one, two = self._node_counts_aux(node._left)
            one += 1

        elif node._left is None and node._right is not None:

            zero, one, two = self._node_counts_aux(node._right)
            one += 1

        else:

            zero_l, one_l, two_l = self._node_counts_aux(node._left)
            zero_r, one_r, two_r = self._node_counts_aux(node._right)
            zero = zero_l + zero_r
            one = one_l + one_r

            two = two_l + two_r + 1

        return zero, one, two

    def mirror(self):
        """
        ---------------------------------------------------------
        Creates a mirror version of a BST. All nodes are swapped 
        with nodes on the other side the tree. Nodes may take the
        place of an empty spot.
        The resulting tree is a mirror image of the original tree.
        (Note that the mirrored tree is not a BST). The original 
        BST is unchanged.
        Use: tree = bst.mirror()
        ---------------------------------------------------------
        Returns:
            tree - a mirror version of BST
        ---------------------------------------------------------
        """
        tree = BST()
        tree._root = self._mirror_aux(self._root)
        return tree

    def _mirror_aux(self, node):
        """
        ---------------------------------------------------------
        Creates a mirror version of a subtree rooted at node. All
        nodes are swapped with nodes on the other side the tree. 
        Nodes may take the place of an empty spot. The resulting 
        tree is a mirror image of the original tree. 
        Use: self._mirror_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - a binary search tree node (BSTNode)
        Returns:
            tree - a mirror version of subtree rooted at node.
        ---------------------------------------------------------
        """
        if node is not None:
            new_node = _BST_Node(node._value)
            new_node._right = self._mirror_aux(node._left)
            new_node._left = self._mirror_aux(node._right)
        else:
            new_node = None
        return new_node

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of the subtree
        rooted at node - handles empty node.
        Private operation called only by other methods.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (BSTNode)
        Returns:
            height - the height of the subtree rooted at node,
             0 if node is None,  (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def find_r(self, element):
        """
        -------------------------------------------------------
        finds the node containing the given element in a BST.
        (Recursive)
        Use: node = bst.find_r(element)
        -------------------------------------------------------
        Parameters:
            element - a data element to search for (?)
        Returns:
            node - If bst contains key, returns value, else 
            returns None.
        -------------------------------------------------------
        """
        node = self._find_r_aux(self._root, element)
        return node

    def _find_r_aux(self, current, element):
        """
        -------------------------------------------------------
        find the given element in a BST rooted at current
        -------------------------------------------------------
        Parameters:
            current - a bst node (_BST_Node)
            element - data element to search for (?)
        Returns:
            node - contains element, else returns None (?)
        -------------------------------------------------------
        """
        if current is None:
            # Base case: at bottom of tree and key not found.
            node = None
        else:
            if element < current._value:
                node = self._find_r_aux(current._left, element)
            elif element > current._value:
                node = self._find_r_aux(current._right, element)
            else:
                node = deepcopy(current._value)
        return node

    def average_height(self):
        """
        ---------------------------------------------------------
        Returns the average height of a bst.
        ---------------------------------------------------------
        Returns:
            avg_height - total height count divided by the number of nodes
                in the tree (int)
        ---------------------------------------------------------
        """

        count = self._count


    def preorder_i(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        (Iterative algorithm)
        Use: bst.preorder_i()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """

        #your code goes here


    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in bst (int)
        ----------------------------------------------------------
        """
        number = self._count_aux(self._root)
        return number

    def _count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a subtree rooted at node
        -------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            number - count of nodes in the subtree rooted at node (int)
        ----------------------------------------------------------
        """
        if node is None:
            # Base case: node does not exist
            number = 0
        else:
            # General case: node exists.
            number = 1 + self._count_aux(node._left) + \
                self._count_aux(node._right)
        return number

    def count_apply(self, func):
        """
        ---------------------------------------------------------
        Returns the number of data elements in a BST where 
        func(element) is True.
        Use: number = bst.count_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a data element in the bst
                returns True for some condition, otherwise returns False.
        Returns:
            number - count of nodes in tree where func(element) is True (int)
        ----------------------------------------------------------
        """
        number = self._count_apply_aux(func, self._root)
        return number

    def _count_apply_aux(self, func, node):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a subtree rooted at node
        where the result of calling func(value) is True.
        Use: number = self.__count_apply_aux(func, node)
        -------------------------------------------------------
        Parameters:
            node - a BST node (BSTNode)
        Returns:
            number - count of nodes in the subtree rooted at node (int)
        ----------------------------------------------------------
        """
        if node is None:
            # Base case: node does not exist
            number = 0
        else:
            # General case: node exists.
            if func(node._value):
                number = 1
            else:
                number = 0
            number = number + self._count_apply_aux(func, node._left) + \
                self._count_apply_aux(func, node._right)
        return number


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._data

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
