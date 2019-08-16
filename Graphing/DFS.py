# mark the current vertex as being visited
# explore each adjecent vertex that is not included in the visited set

# from .graph import Graph 
from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited = 1 
    visited = 2 
    visiting = 3 

class Node:
    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.connectedTo = OrderedDict() #key = node, value = weight

    def __str__(self):
        return str(self.num)

    def getConnections(self):
        return [i.num for i in self.connectedTo.keys()]

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    # this allows us to use in method, like for object in Graph, meaning for object in self.vertList.values()
    def __iter__(self):
        return iter(self.nodes.values())

    def __contains__(self, node):
        return node in self.nodes

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node 

    def add_edge(self, source, dest, weight=0):

        # taken into account when the source and dest are not in the nodes
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].connectedTo[self.nodes[dest]] = weight


        
def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph.nodes[vertex].getConnections()) - set(visited))   #set difference
            
    return visited 

def dfs_paths(graph, start, goal):
    result = []
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()
        for nxt in set(graph.nodes[vertex].getConnections()) - set(path):
            if nxt == goal:
                result.append(path + [nxt]) # could use yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

    return result


g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 

# print(dfs(g,2))
print(dfs_paths(g, 0, 2))











