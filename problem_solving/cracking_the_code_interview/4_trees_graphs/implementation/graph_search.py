from typing import List, Tuple
from collections import deque


class GraphNode:
    def __init__(self, val, adjacent=None):
        self.val = val
        self.adjacent: List[GraphNode] = adjacent if adjacent is not None else []

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Graph:
    def __init__(self, nodes):
        self.nodes: List[GraphNode] = nodes
        self.edges: List[Tuple[GraphNode, GraphNode]] = []

    def add_edge(self, node1: GraphNode, node2: GraphNode):
        # adds a directed edge
        self.edges.append((node1, node2))
        node1.adjacent.append(node2)


def DFS_recursive(root: GraphNode, visited_):
    print(root.val)
    visited_[root] = True
    for node in root.adjacent:
        if not visited_[node]:
            DFS_recursive(node, visited_)


def DFS_iterative(G: Graph, root: GraphNode):
    visited_ = dict(zip(G.nodes, [False for _ in G.nodes]))
    stack = []
    traversed = []
    visited_[root] = True
    traversed.append(root)
    stack.append((root, 0))
    while stack:
        node, pos = stack.pop()
        if pos < len(node.adjacent):
            child = node.adjacent[pos]
            stack.append((node, pos + 1))
            if not visited_[child]:
                visited_[child] = True
                traversed.append(child)
                stack.append((child, 0))
    return traversed


def BFS_iterative(G: Graph, root: GraphNode):
    discovered = dict(zip(G.nodes, [False for _ in G.nodes]))
    discovered[root] = True
    traversed = []
    q = deque([root])
    while q:
        curr = q.popleft()   # take the node from queue
        traversed.append(curr.val)  # it is now traversed
        for node in curr.adjacent:
            if not discovered[node]:
                discovered[node] = True  # the node is discovered
                q.append(node)  # now it's added to the queue to be traversed
    return traversed


if __name__ == '__main__':
    graph = Graph(nodes=[GraphNode(0), GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4), GraphNode(5)])
    """
    0  -->  1  <--   2
    |  \\   |   \\   ^
    v   \\  v    \\v |
    5       4  <--   3
    """
    graph.add_edge(graph.nodes[0], graph.nodes[1])
    graph.add_edge(graph.nodes[0], graph.nodes[4])
    graph.add_edge(graph.nodes[0], graph.nodes[5])
    graph.add_edge(graph.nodes[1], graph.nodes[3])
    graph.add_edge(graph.nodes[1], graph.nodes[4])
    graph.add_edge(graph.nodes[2], graph.nodes[1])
    graph.add_edge(graph.nodes[3], graph.nodes[2])
    graph.add_edge(graph.nodes[3], graph.nodes[4])

    visited = dict(zip(graph.nodes, [False for _ in graph.nodes]))
    DFS_recursive(graph.nodes[0], visited)

    print(DFS_iterative(graph, graph.nodes[0]))
    print(BFS_iterative(graph, graph.nodes[0]))
