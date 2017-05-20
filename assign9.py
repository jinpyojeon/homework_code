#!/usr/bin/python

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


class Edge:
    def __init__(self, source, to, weight):
        self.source = source
        self.to = to
        self.weight = weight

class Graph:

    def __init__(self):
        self.numNodes = 0
        self.adjList = [] 

    def getEdge(self, i, j):
        for node in self.adjList[i]:
            if node.data and node.data.to == j:
                return edge.data.weight

    def incoming(self, i):
        result = [] 
        for node in self.adjList[i]:
            if node.data.source == i:
                result.append(node.data)
        return result

    def outgoing(self, i):
        result = []
        for node in self.adjList[i]:
            if node.data and node.data.to == i:
                result.append(node.data)
        return result

    def addNode(self):
        self.numNodes += 1
        self.adjList.append(LinkedList())
    
    def addEdge(self, source, to, weight):
        self.adjList[source].add_node(Edge(source, to, weight))
        self.adjList[to].add_node(Edge(source, to, weight))

def BFS(G, start): 
    visited = {}
    visited[start] = 1
    queue = [] 
    queue.insert(0, start)
    while queue:
        j = queue.pop()
        print j
        visited[j.data.to] = 1
        for node in G.outgoing(j.data.to):
            if node not in visited:
                queue.insert(0, node)

def main():
    g = Graph()
    g.addNode()
    g.addNode()
    g.addNode()
    g.addEdge(1,2,3)
    g.addEdge(2,1,4)
    BFS(g, 1)



if __name__ == '__main__':
    main()