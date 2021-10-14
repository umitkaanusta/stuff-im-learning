from collections import deque

"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""


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


def find_route(G: Graph, node1: GraphNode, node2: GraphNode):
    # Do BFS from node1
    # Path from node1 to node2 will be node1 -> node2 since the graph is directed
    # If it was undirected, we would do bidirectional BFS, but now we'll just do BFS from node1.
    if node1 == node2:
        return True
    discovered = dict(zip(G.nodes, [False for _ in G.nodes]))
    discovered[node1] = True
    q = deque([node1])
    while q:
        curr = q.popleft()
        for node in curr.adjacent:
            if not discovered[node]:
                if node == node2:
                    return True
                discovered[node] = True
                q.append(node)
    return discovered[node2]


def test_solution():
    graph = Graph(nodes=[None, GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4),
                         GraphNode(5), GraphNode(6), GraphNode(7)])
    """
     -> 4 -> 6
   1            \
    \ -> 2 -> 3 <- 5
     \
      > 7
    """
    graph.add_edge(graph.nodes[1], graph.nodes[4])
    graph.add_edge(graph.nodes[1], graph.nodes[2])
    graph.add_edge(graph.nodes[1], graph.nodes[7])
    graph.add_edge(graph.nodes[4], graph.nodes[6])
    graph.add_edge(graph.nodes[2], graph.nodes[3])
    graph.add_edge(graph.nodes[7], graph.nodes[3])
    graph.add_edge(graph.nodes[6], graph.nodes[5])
    graph.add_edge(graph.nodes[5], graph.nodes[3])
    assert find_route(graph, graph.nodes[1], graph.nodes[5])
    assert not find_route(graph, graph.nodes[2], graph.nodes[7])


if __name__ == '__main__':
    test_solution()
