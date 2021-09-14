import queue


# Referenced from: https://stackoverflow.com/questions/43354715/uniform-cost-search-in-python
# Node data structure
class Node:
    def __init__(self, label):
        self.out_edges = []
        self.label = label
        self.is_goal = False

    def add_edge(self, node, weight=0):
        self.out_edges.append(Edge(node, weight))


# Edge data structure
class Edge:
    def __init__(self, node, weight=0):
        self.node = node
        self.weight = weight

    def to(self):
        return self.node


# Graph data structure, utilises classes Node and Edge
class Graph:
    def __init__(self):
        self.nodes = []

    # some other functions here populate the graph, and randomly select three goal nodes.


def ucs(G, v):
    visited = set()  # set of visited nodes
    fringe = queue.PriorityQueue()
    # (cost, n, path)
    # cost: the cumulative cost,
    # n: the current node,
    # path: the path that led to the expansion of the current node
    fringe.put((0, v, [v]))

    while not fringe.empty():  # while the queue is not nempty
        cost, current_node, path = fringe.get()
        visited.add(current_node)  # mark node visited on expansion,
        # only now we know we are on the cheapest path to
        # the current node.

        if current_node.is_goal:  # if the current node is a goal
            return path  # return its path
        else:
            for edge in current_node.out_edges:
                child = edge.to()
                if child not in visited:
                    fringe.put((cost + edge.weight, child, path + [child]))
