from py_btree_node import node

class bstree:
    def __init__(self):
        self.root = None

    def search_helper(self, n, curr):
        try:
            if curr.get_key() == n.get_key():
                return curr
            if curr.get_key() < n.get_key():
                if curr.get_right() is None:
                    return curr
                return self.search_helper(n, curr.get_right())
            if curr.get_key() > n.get_key():
                if curr.get_left() is None:
                    return curr
                return self.search_helper(n, curr.get_left())
        except AttributeError:
            raise Exception("The tree is empty")
            
        
    def search(self, n):
        """Takes a node n and:
        - if there is a node m with the same key in the tree, it returns m.
        - otherwise (assuming the tree is not empty), it returns the node that would be n's parent,
        if n was inserted to the tree at its current state."""
        return self.search_helper(n, self.root)
        
    
    def insert(self, elem):
        """Takes a pair (list/tuple/dictionary) of key and value and adds \
        appropriate node to tree."""
        if type(elem) is dict: #elem is a dictionary
            key = elem.keys()[0]
            val = elem[key]
        else: #elem is a list/tuple
            try:
                key = elem[0]
                val = elem[1]
            except TypeError, IndexError:
                raise Exception("Element passed to insert should be pair (list/tuple/dictionary)\
                                of key and value")
        new_node = node()
        new_node.set_key(key)
        new_node.set_value(val)

        if self.root is None:
            self.root = new_node
            return

        result = self.search(new_node)

        if result.get_key() == new_node.get_key():
            return
        else:
            new_node.set_parent(result)
            if new_node.get_key() > result.get_key():
                result.set_right(new_node)
                return
            result.set_left(new_node)
        return

    def min_in_subtree(self, sub_root):
        """Takes root of a subtree and returns node with minimal key in the subtree."""
        if sub_root is None:
            return None
        while sub_root.get_left() is not None:
            sub_root = sub_root.get_left()
        return sub_root

    def max_in_subtree(self, sub_root):
        """Takes root of a subtree and returns node with maximal key in the subtree."""
        if sub_root is None:
            return None
        while sub_root.get_right() is not None:
            sub_root = sub_root.get_right()
        return sub_root
        
    def remove(self, key):
        """Takes a key and removes a node with the same key from the tree. (while maintaining a valid[legal] search tree structure)
           If there is no such node in the tree, the tree is left unchanged."""
        n_to_remove = node(key)
        search_result = self.search(n_to_remove)
        if search_result.get_key() != key: #the key is not in the tree
            return
        elif (search_result.get_right() is None) and (search_result.get_left() is None): #removing a leaf
            if search_result.get_parent() is None: #we want to remove root
                self.root = None
                return
            if search_result.get_parent().get_key() > search_result.get_key(): #element we want to remove is the left son
                search_result.get_parent().set_left(None)
                search_result.set_parent(None)
                return
            search_result.get_parent().set_right(None) #element we want to remove is the right son
            search_result.set_parent(None)
            return
        elif search_result.get_right() is None: #only left son
            search_result.get_left().set_parent(search_result.get_parent())
            if search_result.get_parent() is not None:
                if search_result.get_parent().get_key() > search_result.get_key(): #removing a left son
                    search_result.get_parent().set_left(search_result.get_left())
                else: #removing a right son
                    search_result.get_parent().set_right(search_result.get_left())
            else: #removed root
                self.root = search_result.get_left()
                if self.root.get_right() is not None:
                    self.root.get_right().set_parent(self.root)
                if self.root.get_left() is not None:
                    self.root.get_left().set_parent(self.root)
            search_result.set_left(None)
            search_result.set_parent(None)
            return
        elif search_result.get_left() is None: #only right son
            search_result.get_right().set_parent(search_result.get_parent())
            if search_result.get_parent() is not None:
                if search_result.get_parent().get_key() > search_result.get_key(): #removing a left son
                    search_result.get_parent().set_left(search_result.get_right())
                else: #removing a right son
                    search_result.get_parent().set_right(search_result.get_right())
            else: #removed root
                self.root = search_result.get_right()
                if self.root.get_left() is not None:
                    self.root.get_left().set_parent(self.root)
                if self.root.get_right() is not None:
                    self.root.get_right().set_parent(self.root)
            search_result.set_right(None)
            search_result.set_parent(None)
            return
        else: #two sons - binary node
            min_right = self.min_in_subtree(search_result.get_right()) #find the min in the right subtree
            #remove min_right node
            if min_right.get_key() < min_right.get_parent().get_key(): #min_right is left son
                min_right.get_parent().set_left(min_right.get_right())
            else: #min_right is right son
                min_right.get_parent().set_right(min_right.get_right())
            min_right.set_parent(None)
            #put min_right in the place of the node to remove
            search_result.set_key(min_right.get_key())
            search_result.set_value(min_right.get_value())
    

    def find(self, key):
        """Takes a key and returns the value of a node with the same key in the tree. If there is no such node, a KeyError exception is raised."""
        search_result = self.search(node(key))
        if search_result.get_key() == key: #the given key was found in the tree
            return search_result.get_value()
        #the given key was not found in the tree
        raise KeyError('{}, no such key'.format(key))

    def __repr__(self):
        return "Instance of bstree (binary search tree)"

    def rec_str(self, curr):
        if curr is None:
            return ''
        return self.rec_str(curr.get_left()) + '{%s:%s}' % (curr.get_key(), curr.get_value()) + self.rec_str(curr.get_right())
    
    def __str__(self):
        return 'The tree nodes in a {key:value} format, in left-middle-right order:\n' + self.rec_str(self.root)

    def rec_iter(self, curr):
        if curr is None:
            return []
        return self.rec_iter(curr.get_left()) + [{curr.get_key():curr.get_value()}] + self.rec_iter(curr.get_right())
    
    def __iter__(self):
        """Returns an iterator that goes over all nodes in left-middle-right order, there is a respective dictionary for each node."""
        return iter(self.rec_iter(self.root))
            
            
        
        
            
            
        
