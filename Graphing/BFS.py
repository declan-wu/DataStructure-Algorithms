# This article is excellent in explaining DFS and BFS: https://jeremykun.com/2013/01/22/depth-and-breadth-first-search/
import Graphing.Graph_ADT


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(
                set(graph.nodes[vertex].getConnections()) - set(visited))

    return visited


def bfs_paths(graph, start, goal):
    result = []
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        for nxt in set(graph.nodes[vertex].getConnections()) - set(path):
            if nxt == goal:
                result.append(path + [nxt])  # could use yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))

    return result


def shortest_path(graph, start, goal):
    try:
        return (bfs_paths(graph, start, goal))[0]
    except StopIteration:
        return None


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(3, 5)

print(shortest_path(g, 0, 5))
