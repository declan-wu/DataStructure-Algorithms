# mark the current vertex as being visited
# explore each adjecent vertex that is not included in the visited set

# from .graph import Graph
from enum import Enum
from collections import OrderedDict
import Graphing.Graph_ADT


def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # set difference
            stack.extend(
                set(graph.nodes[vertex].getConnections()) - set(visited))
    return visited


def dfs_paths(graph, start, goal):
    result = []
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in set(graph.nodes[vertex].getConnections()) - set(path):
            if nxt == goal:
                result.append(path + [nxt])  # could use yield path + [nxt]
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
