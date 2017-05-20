#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class Node:
    def __init__(self):
        self.data = None # contains the data
        self.prev = None
        self.next = None # contains the reference to the next node

# Implementation of doubly linked list in Python
class LinkedList:
    # Self is like this keyword in C++ - refers to the instantiated 
    # object of the class 
    # Properties of the object are denoted self.{property} 
    def __init__(self):
        self.head_node = Node()
        self.tail_node = Node()

        self.head_node.next = self.tail_node
        self.tail_node.prev = self.head_node
        
        self.cur_node = self.head_node

    def add_node(self, data):
        # Initializing new node
        new_node = Node() # create a new node
        new_node.data = data
        new_node.next = self.tail_node # link the new node to the 'previous' node.
        new_node.prev = self.tail_node.prev
        
        # Setting new node to be the last node
        self.tail_node.prev.next = new_node
        self.tail_node.prev = new_node
    
    def delete_node(self, node):
        node.prev.next = node.next

    def __iter__(self):
        start = self.tail_node
        while start.prev:
            start = start.prev
            yield start
        raise StopIteration 

# Way to declare abstract class in Python
class Set():
    __metaclass__ = ABCMeta

    @abstractmethod
    def contains(self,x): pass

    @abstractmethod
    def insert(self, x): pass

    @abstractmethod
    def delete(self, x): pass

    @abstractmethod
    def __iter__(self): pass

    # For iterator, see:https://www.programiz.com/python-programming/iterator

class ListSet(Set):

    def __init__(self):
        self.linked_list = LinkedList()

    def contains(self, x): 
        for e in self.linked_list:
            if x == e.data:
                return True
        return False

    def insert(self, x):
        self.linked_list.add_node(x)
    
    def delete(self, x):
        for e in self.linked_list:
            if e.data == x:
                self.linked_list.delete_node(e)
    
    def __iter__(self):
        for each in self.linked_list:
            if each.data:
                yield each.data
            else:
                raise StopIteration 
def main():
    test = ListSet()
    test.insert(4)
    test.insert(2)
    test.insert(4)
    test.insert(6)
    test.insert(7)
    for i in test:
        print i

class BST(Set):

    def __init__(self):
        self.tree = Tree()
    
    def contains(self, x):
    
    def insert(self, x):

    def delete(self, x):

    def __iter__(self):
        traverse_left(self.tree)
    
    def traverse_left(root):
        if (root.left) traverse_left(root.left)
        yield root
        if (root.right) traverse_left(root.right)
        raise StopIteration

if __name__ == '__main__':
    main()

