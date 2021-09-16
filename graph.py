# Node data structure
class Node:
    def __init__(self, label):
        self.out_edges = []
        self.label = label
        self.is_goal = False
        self.heuristic_value = -1

    def add_edge(self, node, weight=0):
        self.out_edges.append(Edge(node, weight))

    def modify_heuristic_value(self, heuristic_value):
        self.heuristic_value = float(heuristic_value)


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
        origin_node = self.node(origin_label)
        origin_node.is_goal = is_goal
        destination_node = self.node(destination_label)
        origin_node.add_edge(destination_node, float(cost))
        destination_node.add_edge(origin_node, float(cost))

        if origin_node not in self.nodes:
            self.nodes.append(origin_node)
        if destination_node not in self.nodes:
            self.nodes.append(destination_node)

    # this function prints graph
    def print_graph(self):
        for node in self.nodes:
            out_edges_labels = []
            for edge in node.out_edges:
                out_edges_labels.append({edge.to(), edge.weight})
            print(
                "Origin: "
                + node.label
                + " | {Weight, Destination}: "
                + str(out_edges_labels)
                + " | is_goal? "
                + str(node.is_goal)
                + " | heuristic_value: "
                + str(node.heuristic_value)
            )
