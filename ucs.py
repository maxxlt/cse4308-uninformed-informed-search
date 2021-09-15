
# Referenced from: https://stackoverflow.com/questions/43354715/uniform-cost-search-in-python
# to implement node and edges to the node

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


class Graph:

    def __init__(self):
        self.nodes = []

    def contains(self, label):
        for node in self.nodes:
            if node.label == label:
                return True
        return False

    # this function checks whether or not the node exists in the `self.nodes`,
    # if it is, return the address of that node,
    # otherwise return new Node() object with given label
    # Side note: this function prevents from adding existing node in `self.nodes`
    def node(self, label):
        for node in self.nodes:
            if node.label == label:
                return node
        return Node(label)

    # this function adds a new node with given information passed as arguments
    def add_new_node(self, origin_label, destination_label, cost, is_goal):
        node = self.node(origin_label)
        node.is_goal = is_goal  # reassigning is_goal, better solution?
        node.add_edge(self.node(destination_label), float(cost))
        if (node not in self.nodes):  # if node node not in `self.nodes`, we add that node in
            self.nodes.append(node)
        if (self.node(destination_label) not in self.nodes):
            self.nodes.append(self.node(destination_label))
        if (node not in self.node(destination_label).out_edges):
            self.node(destination_label).add_edge(node, float(cost))

    # this function prints graph
    def print_graph(self):
        for node in self.nodes:
            out_edges_labels = []
            for edge in node.out_edges:
                out_edges_labels.append({edge.to(), edge.weight})
            print("Origin: " + node.label + " | {Weight, Destination}: " + str(out_edges_labels) +
                  " | is_goal? " + str(node.is_goal))
